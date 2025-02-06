"""Link Handling"""

from modules.logger import global_logger as logger
from modules.doc_handling import replace_doc
from modules.img_handling import replace_images


def link_to_md(element):
    """
    Converts an HTML anchor element into a Markdown link.

    Args:
        element (a element): A Link on the Wiki page

    Returns:
        str: Markdown-formatted link.
    """
    try:
        if element is None:
            logger.warning("Link-Element ist None, wird ignoriert.")
            return ""

        logger.debug(f"Verarbeite Link: {element.get_text(strip=True)}")

        if "confluence-embedded-file" in element.get("class", []):
            logger.info("Eingebettete Datei erkannt, wird verarbeitet...")
            md_link = replace_doc(element)
        else:
            text = element.get_text(strip=True)
            href = element.get("href", "")

        if not href:
            logger.warning(f"Link ohne href-Attribut erkannt: {text}")
            href = "nolink"
        
        if url.startswith("/wiki/"):
            url = f"https://de.wikipedia.org{url}"
            md_link = f"[{text}]({url})"

        # Sonderfall: Wenn der Link eine Bilddatei enthält
        if "Datei:" in href:
            child = element.find("img")
            md_link = replace_images(child)
        elif "@" in text:
            md_link = f" [{text}](mailto:{text})"
        else:
            md_link = f"[{text}]({href})"

        logger.info(f"Link erfolgreich konvertiert: {md_link}")
        return md_link

    except Exception as e:
        logger.error(f"Fehler bei der Link-Konvertierung: {str(e)}")
        return ""
