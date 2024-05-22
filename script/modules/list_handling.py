"""List Handling"""

from bs4 import NavigableString, Tag
from modules.text_handling import (
    formatting_to_md,
    headers_to_markdown,
    escape_html_tags,
)
from modules.img_handling import replace_images
from modules.link_handling import link_to_md
from modules.link_handling import jira_to_md
from modules.code_handling import code_to_md
from modules.macro_handling import macro_to_md
from modules.blockquote_handling import blockquote_to_md
from modules.gliffy_handling import gliffy_warning
from modules.table_handling import table_to_md


def list_to_md(input, target_url, ebene=0):
    """
    Converts a list element on the Confluence Page to markdown

    Args:
        element (ul/ol element): The list element that needs to be converted
        ebene (int, optional): Depth of the list. Defaults to 0.

    Returns:
        String: Markdown Syntax for Lists
    """

    if input.name == "ol":
        return ordered_list_to_md(input, target_url, ebene)

    liste = ""
    einrueckung = "  " * ebene  # Verwendet Leerzeichen für die Einrückung

    for element in input.find_all(
        recursive=False
    ):  # Verhindert, dass tiefer liegende <li> direkt verarbeitet werden
        item = search_child(element, target_url, ebene)
        # Füge den Markdown für das aktuelle Element hinzu, mit Einrückung und ggf. Unterlisten
        if element.name != "li":
            liste += f"{einrueckung} {item}\n"
        else:
            liste += f"{einrueckung}* {item}\n"

    return liste


def search_child(element, target_url, depth=0):

    element_to_markdown_converter = {
        "a": link_to_md,
        "code": code_to_md,
        "blockquote": blockquote_to_md,
        "img": replace_images,
        "u": formatting_to_md,
        "strong": formatting_to_md,
        "s": formatting_to_md,
        "em": formatting_to_md,
        "h1": headers_to_markdown,
        "h2": headers_to_markdown,
        "h3": headers_to_markdown,
        "h4": headers_to_markdown,
        "h5": headers_to_markdown,
        "h6": headers_to_markdown,
    }

    markdown = ""

    if isinstance(element, Tag):
        converter = element_to_markdown_converter.get(element.name)
        if converter:
            conversion_result = converter(element)
            if conversion_result is not None:
                markdown += conversion_result
        elif not element.children:
            text = element.get_text(strip=True)
            if text:
                markdown += text
        elif element.name == "table":
            markdown += table_to_md(element, target_url)
        elif element.name == "ul":
            markdown += "\n" + list_to_md(element, target_url, depth + 1)
        elif element.name == "ol":
            markdown += "\n" + ordered_list_to_md(element, target_url, depth + 1)
        elif not converter and element.children:
            if "class" in element.attrs and "gliffy-container" in " ".join(
                element["class"]
            ):
                markdown += gliffy_warning(target_url)
            elif "class" in element.attrs and "code" in " ".join(element["class"]):
                markdown += code_to_md(element)
            elif "class" in element.attrs and "macro" in " ".join(element["class"]):
                markdown += "\n" + macro_to_md(element, target_url)
            elif "class" in element.attrs and "jira-issue" in " ".join(
                element["class"]
            ):
                markdown += jira_to_md(element)
            else:
                for child in element.children:
                    markdown += search_child(child, target_url, depth)
    elif isinstance(element, NavigableString):
        text = element.strip()
        text = escape_html_tags(text)
        if text:
            markdown += text

    return markdown


def ordered_list_to_md(input, target_url, depth):
    liste = ""
    einrueckung = "   " * depth  # Verwendet Leerzeichen für die Einrückung
    number = 1
    for element in input.find_all(
        recursive=False
    ):  # Verhindert, dass tiefer liegende <li> direkt verarbeitet werden
        item = search_child(element, target_url, depth)
        if element.name != "li":
            liste += f"{einrueckung} {item}\n"
        else:
            liste += f"{einrueckung}{number}. {item}\n"
            number += 1

    return liste
