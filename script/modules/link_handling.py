"""Link Handling"""

from modules.logger import logger  # Logger importieren
from modules.doc_handling import replace_doc
from modules.img_handling import replace_images


def link_to_md(element):
    """
    Converts an HTML anchor element into a Markdown link. If the element has a
    class 'confluence-embedded-file', it uses a document handler to replace the
    document reference. Otherwise, it creates a Markdown link either as a MailTo
    link if the content contains an email address or a standard link otherwise.

    Args:
        element (Tag): A link element from the Confluence page.

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


def jira_to_md(element):
    """
    Converts a Confluence Jira issue link into Markdown.

    Args:
        element (Tag): The Jira issue link element.

    Returns:
        str: Markdown-formatted Jira issue link.
    """
    try:
        if element is None:
            logger.warning("Jira-Element ist None, wird ignoriert.")
            return ""

        ticket = element.find("a")

        if ticket is None:
            logger.warning("Kein <a>-Tag innerhalb des Jira-Elements gefunden.")
            return ""

        logger.debug(f"Verarbeite Jira-Link: {ticket.get_text(strip=True)}")

        jira_link = link_to_md(ticket)

        logger.info(f"Jira-Link erfolgreich konvertiert: {jira_link}")
        return jira_link

    except Exception as e:
        logger.error(f"Fehler bei der Jira-Link-Konvertierung: {str(e)}")
        return ""
