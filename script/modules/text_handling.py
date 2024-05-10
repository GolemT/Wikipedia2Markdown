"""Text Handling"""

import re
from bs4 import Tag


def headers_to_markdown(element):
    """
    Converts HTML header elements (h1 to h6) to their equivalent Markdown format.
    Checks if the element is one of the header tags, processes only text-based headers,
    and ignores headers with nested tags. It formats the header according to its level,
    applying appropriate Markdown syntax.

    Args:
        element (h element): HTML element of a header

    Returns:
        String | None: Markdown Syntax for headers
    """
    if element.name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
        if any(isinstance(child, Tag) for child in element.children):
            return None

        elif element.get_text(strip=True):
            level = int(element.name[1])
            text = formatting_to_md(element)
            markdown_header = (
                "#" * level + " " + text + "\n"
            )  # Titel können ebenfalls unterstrichen sein
            return markdown_header
    else:
        return None


def formatting_to_md(element):
    """
    Converts HTML formatting elements (s, strong, u, em) to their Markdown or HTML equivalents.
    Appends formatting markers based on the element's tag and nested tags, wraps the text content
    appropriately, and ensures correct closure of tags in the formatted string.

    Args:
        element (s element | strong | u | em): HTML element with formatted text

    Returns:
        String: Markdown Syntax for differently formatted text
    """
    format_symbol = ""
    if element.name == "s":
        format_symbol += "~~"
    elif element.name == "strong":
        format_symbol += "**"
    elif element.name == "u":
        format_symbol += "<u>"
    elif element.name == "em":
        format_symbol += "_"

    for child in element.children:
        if child.name == "s":
            format_symbol += "~~"
        if child.name == "strong":
            format_symbol += "**"
        if child.name == "u":
            format_symbol += "<u>"
        if child.name == "em":
            format_symbol += "_"

    md = f""" {format_symbol}
    {escape_html_tags(element.get_text(strip=True))}
    {format_symbol[::-1].replace(">u<", "</u>")} """
    return md


# clean_title: Cleans the title string by using a regular expression to remove specific characters.
# It takes a title string as input and returns the cleaned title string.
def clean_str(element):
    """
    Function to convert a String with special characters into a string that
    can be displayed without any errors

    Args:
        element (String): Input String with special characters like %

    Returns:
        String: Input String without any special characters
    """
    regex_pattern = r"[^a-zA-Z0-9\s\.]"
    cleaned_string = re.sub(regex_pattern, " ", element).strip().replace(" ", "_")

    return escape_html_tags(cleaned_string)


def escape_html_tags(text):
    """
    Escapes HTML tags in the provided text by replacing '<' and '>' with their HTML entities.

    Args:
        text (String): Text that may contain Elements that should not be computed

    Returns:
        String: Text with escaped HTML elements
    """
    # Replace '<' and '>' with their corresponding HTML entities
    wip_text = re.sub(r"<", "&lt;", text)
    wip_text = re.sub(r">", "&gt;", wip_text)

    return wip_text
