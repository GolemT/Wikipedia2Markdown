"""Link Handling"""

from modules.logger import global_logger as logger
from modules.img_handling import replace_images


def link_to_md(element):
    """
    Converts an HTML anchor element into a Markdown link. If the element has a
    class 'Wikipedia-embedded-file', it uses a document handler to replace the
    document reference. Otherwise, it creates a Markdown link either as a MailTo
    link if the content contains an email address or a standard link otherwise.

    Args:
        element (Tag): A link element from the Wikipedia page.

    Returns:
        str: Markdown-formatted link.
    """
    try:
        if element is None:
            logger.warning("Link-Element ist None, wird ignoriert.")
            return ""

        logger.debug(f"Verarbeite Link: {element.get_text(strip=True)}")

        text = element.get_text(strip=True)
        href = element.get("href", "")

        if not href:
            logger.warning(f"Link ohne href-Attribut erkannt: {text}")
            href = "nolink"
        
        if href.startswith("/wiki/"):
            href = f"https://de.wikipedia.org{href}"
            md_link = f"[{text}]({href})"

        # Sonderfall: Wenn der Link eine Bilddatei enthält
        if "Datei:" in href:
            child = element.find("img")
            md_link = replace_images(child)
        elif "@" in text:
            md_link = f" [{text}](mailto:{text})"
        else:
            md_link = f"[{text}]({href})"
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
