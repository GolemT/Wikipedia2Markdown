"""Link-Verarbeitung"""

from modules.logger import global_logger as logger
from modules.img_handling import replace_images


def link_to_md(element):
    """
    Konvertiert ein HTML-Anchor-Element in einen Markdown-Link. Wenn das Element die
    Klasse 'Wikipedia-embedded-file' hat, verwendet es einen Dokumentenhandler, um die
    Dokumentreferenz zu ersetzen. Andernfalls erstellt es einen Markdown-Link entweder als
    MailTo-Link, wenn der Inhalt eine E-Mail-Adresse enthält, oder als Standardlink.

    Args:
        element (Tag): Ein Link-Element von der Wikipedia-Seite.

    Returns:
        str: Markdown-formatierter Link.
    """
    try:
        if element is None:
            logger.warning("Link-Element ist None, wird ignoriert.")
            return ""

        if "class" in element.attrs and 'mw-jump-link' in element["class"]:
            logger.info("Link-Element hat class, wird ignoriert.")
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

        logger.info(f"Link erfolgreich konvertiert: {md_link}")
        return md_link

    except Exception as e:
        logger.error(f"Fehler bei der Link-Konvertierung: {str(e)}")
        return ""
