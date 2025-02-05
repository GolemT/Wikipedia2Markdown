"""Table Handling"""

from bs4 import BeautifulSoup, NavigableString
from modules.img_handling import replace_images
from modules.link_handling import link_to_md, jira_to_md
from modules.gliffy_handling import gliffy_warning
from modules.logger import global_logger as logger


def table_to_md(table, target_url):
    """
    Converts a BeautifulSoup table element to a Markdown-compatible format.

    Args:
        table (Tag): BeautifulSoup table element.
        target_url (str): URL needed for Gliffy warnings.

    Returns:
        str: String representation of the modified table.
    """
    try:
        if table is None:
            logger.warning("Kein gültiges Tabellen-Element übergeben.")
            return ""

        logger.debug("Starte Konvertierung einer Tabelle...")

        if "style" in table.attrs:
            del table["style"]

        to_process = table.find_all(True)

        for element in to_process:
            if element.attrs and element.has_attr("style"):
                del element["style"]

            if element.name == "img":
                logger.info("Bild in Tabelle gefunden, wird ersetzt...")
                element.replace_with(replace_images(element))

            elif element.name == "br":
                replacement = "\n" if not element.children else element.get_text()
                element.replace_with(replacement)

            elif element.name == "table":
                logger.debug("Verschachtelte Tabelle erkannt, wird konvertiert...")
                table_text = table_to_md(element, target_url)
                inner_table = BeautifulSoup(table_text, "html.parser")
                element.replace_with(inner_table)

            elif element.name == "a":
                logger.info("Link in Tabelle gefunden, wird konvertiert...")
                element.replace_with(link_to_md(element))

            elif element.attrs:
                class_list = " ".join(element.get("class", []))

                if "jira-issue" in class_list:
                    logger.info("JIRA-Issue in Tabelle gefunden, wird ersetzt...")
                    element.replace_with(jira_to_md(element))

                elif "gliffy-container" in class_list:
                    logger.info("Gliffy-Container in Tabelle gefunden, wird ersetzt...")
                    element.replace_with(gliffy_warning(target_url))

            elif isinstance(element, NavigableString):
                cleaned_text = " ".join(element.string.split())
                element.replace_with(cleaned_text)

        final_table = "".join(str(table).splitlines())
        logger.info("Tabellen-Konvertierung abgeschlossen.")
        return final_table

    except Exception as e:
        logger.error(f"Fehler bei der Tabellen-Konvertierung: {str(e)}")
        return ""
