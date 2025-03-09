"""URL-Verarbeitung"""

import urllib.parse
from modules.logger import global_logger as logger


def url_check(element):
    """
    Stellt die korrekte URL-Formatierung sicher. Wenn die URL bereits eine Abfrage ("?") enthält,
    wird sie unverändert zurückgegeben. Andernfalls wird das letzte Segment nach dem letzten Schrägstrich
    kodiert, um Sonderzeichen zu verarbeiten, und die vollständige URL mit dem kodierten Segment wieder zusammengesetzt.

    Args:
        element (String): Quelle eines HTML-Elements, das eine API-Anfrage enthalten kann.

    Returns:
        String: Formatierte URL ohne API-Anfragen.
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
