"""Blockquote handling"""


def blockquote_to_md(element):
    """
    Convert HTML Blockquote element into markdown syntax

    Args:
        element (blockquote element): the html element to be converted

    Returns:
        String: Markdown syntax of the blockquote element
    """
    quote = ""
    for child in element.find_all():
        if child:
            quote += f"> {child.get_text()}\n"

    return quote
