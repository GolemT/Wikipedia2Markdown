"""Gliffy Handling"""


def gliffy_warning(url):
    """
    Generates a formatted warning message in Markdown to alert users about a missing Gliffy file.
    The warning includes instructions to download the file from a provided Confluence page URL,
    add it to a specific directory, and remove the warning message after the actions are completed.

    Args:
        url (String): Url to the original confluence page for implementing gliffy

    Returns:
        String: Warning message in Markdown
    """

    return f""":::warning Achtung
    Hier fehlt das Gliffy File um das Diagramm anpassen zu können. Bitte gehe auf die [Confluence Seite]({url}), lade das .gliffy file herunter, füge es dem Ordner ``./assets`` hinzu (neben dieser .md Datei) und entferne diesen Hinweis! \n:::"""
