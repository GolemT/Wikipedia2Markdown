"""Blockquote Handling"""

from modules.logger import global_logger as logger


def blockquote_to_md(element):
    """
    Converts an HTML Blockquote element into Markdown syntax.

    Args:
        element (Tag): The HTML blockquote element to be converted.

    Returns:
        str: Markdown syntax of the blockquote element.
    """
    try:
        if element is None:
            logger.warning("Kein gültiges Blockquote-Element übergeben, wird ignoriert.")
            return ""

        logger.debug("Starte Blockquote-Konvertierung...")

        quote = ""
        for child in element.find_all():
            if child:
                quote += f"> {child.get_text().strip()}\n"

        if not quote.strip():
            logger.warning("Leeres Blockquote-Element erkannt, wird ignoriert.")
            return ""

        logger.info(f"Blockquote erfolgreich konvertiert:\n{quote.strip()[:100]}...")  # Kürzung für lesbare Logs
        return quote

    except Exception as e:
        logger.error(f"Fehler bei der Blockquote-Konvertierung: {str(e)}")
        return ""
