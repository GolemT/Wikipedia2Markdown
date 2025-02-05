"""URL Handling"""

import urllib.parse
from modules.logger import logger  # Logger importieren


def url_check(element):
    """
    Ensure proper URL formatting. If the URL already contains a query ("?"), it returns as is.
    Otherwise, it encodes the final segment after the last slash to handle special characters,
    reconstructing the full URL with the encoded segment.

    Args:
        element (String): Source of a HTML element that may contain an API request.

    Returns:
        String: Formatted URL without API requests.
    """
    try:
        if not isinstance(element, str) or not element.startswith("http"):
            logger.warning(f"Ungültige URL erkannt: {element}")
            return element  # Fallback: Gib die URL unverändert zurück

        logger.debug(f"Verarbeite URL: {element}")

        if "?" in element:
            full_url = element
        else:
            first_half = element[:element.rfind("/")]
            parsed_url = urllib.parse.quote(element.split("/")[-1])
            full_url = f"{first_half}/{parsed_url}"

        logger.info(f"URL erfolgreich formatiert: {full_url}")
        return full_url

    except Exception as e:
        logger.error(f"Fehler bei der URL-Verarbeitung: {str(e)}")
        return element  # Falls ein Fehler auftritt, wird die Original-URL zurückgegeben
