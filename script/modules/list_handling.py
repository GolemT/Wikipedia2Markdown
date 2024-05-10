"""List Handling"""

from bs4 import Tag, NavigableString
from modules.link_handling import link_to_md
from modules.code_handling import code_to_md
from modules.macro_handling import macro_to_md
from modules.blockquote_handling import blockquote_to_md
from modules.text_handling import formatting_to_md
from modules.img_handling import replace_images


def list_to_md(element, ebene=0):
    """
    Converts a list element on the Confluence Page to markdown

    Args:
        element (ul/ol element): The list element that needs to be converted
        ebene (int, optional): Depth of the list. Defaults to 0.

    Returns:
        String: Markdown Syntax for Lists
    """

    liste = ""
    einrueckung = "   " * ebene  # Verwendet Leerzeichen für die Einrückung

    for li in element.find_all(
        "li", recursive=False
    ):  # Verhindert, dass tiefer liegende <li> direkt verarbeitet werden
        item = search_child(li, ebene)
        # Füge den Markdown für das aktuelle Element hinzu, mit Einrückung und ggf. Unterlisten
        liste += f"{einrueckung}* {item}\n"

    return liste


def search_child(element, ebene=0):
    """
    extract child elements recursively and return the text within

    Args:
        element (HTML element): Any HTML element that might be in a list
        ebene (int, optional): Depth of the list. Defaults to 0.

    Returns:
        String: Text of the child elements
    """
    text = ""
    for child in element.contents:
        if isinstance(child, NavigableString):
            text += child.strip() + " "
        elif isinstance(child, Tag):
            match child.name:
                case 'h1':
                    text += f'# {child.get_text(strip=True)} \n\n'
                case 'h2':
                    text += f'## {child.get_text(strip=True)} \n\n'
                case 'ul' | 'ol':
                    text += '\n' + list_to_md(child, ebene+1)
                case 'a':
                    text += link_to_md(child)
                case 'br':
                    text += '\n'
                case 'strong' | 'em' | 's' | 'u':
                    text += formatting_to_md(child)
                case 'img':
                    text += replace_images(child) + " "
                case 'blockquote':
                    text += blockquote_to_md(child)
                case _:
                    if 'class' in child.attrs:
                        match ' '.join(child['class']):
                            case classes if 'jira' in classes:
                                pass
                            case classes if 'macro' in classes:
                                if 'code' not in classes:
                                    text += '\n' + macro_to_md(child)
                                else:
                                    text += code_to_md(child)
                            case _:
                                text += search_child(child, ebene)  # Recursively process content
    return text
