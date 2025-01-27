"""Link Handling"""

from doc_handling import replace_doc


def link_to_md(element):
    """
    Converts an HTML anchor element into a Markdown link. If the element has a
    class 'confluence-embedded-file', it uses a document handler to replace the
    document reference. Otherwise, it creates a Markdown link either as a MailTo
    link if the content contains an email address or a standard link otherwise.

    Args:
        element (a element): A Link on the confluence page

    Returns:
        String: Markdown Syntax for Links
    """

    if "confluence-embedded-file" in element.get("class", []):
        md_link = replace_doc(element)

    else:
        text = element.get_text(strip=True)
        if element.get("href", ""):
            url = element.get("href", "")
        else:
            url = "nolink"

        if "@" in text:
            md_link = f" [{text}](mailto:{text})"
        else:
            md_link = f"[{text}]({url})"

    return md_link


def jira_to_md(element):
    """
    Special handling for Jira Tickets

    Args:
        element (HTML element): A element with the link to a jira issue on the confluence page

    Returns:
        String: Markdown Syntax for Links
    """
    ticket = element.find("a")
    ticket = link_to_md(ticket)

    return ticket
