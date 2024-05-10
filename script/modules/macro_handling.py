"""Macro Handling"""

from bs4 import Tag, NavigableString
from modules.text_handling import formatting_to_md
from modules.img_handling import replace_images


def extract_text_recursively(element):
    """
    Extract text from all child elements recursively, handling specific tags appropriately.

    Args:
        element (HTML element): A HTML element with the word "macro" in the class attribute

    Returns:
        String: Formatted element into Markdown
    """
    text = ""
    for child in element.children:
        match child:
            case NavigableString() as ns:
                if ns.name == 'code':
                    from modules.code_handling import code_to_md
                    text += ' ' + code_to_md(ns)
                else:
                    text += ns.strip() + " "
            case Tag() as tag:
                match tag.name:
                    case "h1":
                        text += f"# {tag.get_text(strip=True)} \n\n"
                    case "h2":
                        text += f"## {tag.get_text(strip=True)} \n\n"
                    case "ul":
                        from modules.list_handling import list_to_md
                        text += "\n" + list_to_md(tag)
                    case "a":
                        from modules.link_handling import link_to_md
                        text += " " + link_to_md(tag)
                    case "img":
                        from modules.img_handling import replace_images
                        text += " " + replace_images(tag)
                    case "u" | "strong" | "em" | "s":
                        from modules.text_handling import formatting_to_md
                        text += " " + formatting_to_md(tag)
                    case _:
                        text += extract_text_recursively(tag)
            case _:
                text += extract_text_recursively(child)
    return text


def macro_to_md(element):
    """
    Converts Confluence macro-styled elements to Markdown based on their class attributes.
    Handles specific macro types like warning, error, and info by prepending them with
    appropriate symbols and formatting the content with indentation.

    Args:
        element (HTML Element): A HTML element with the word "macro" in the class attribute

    Returns:
        String: Macro converted to Markdown Syntax
    """

    symbol = ""
    macro_type = ""
    if "class" in element.attrs:
        if "status-macro" in " ".join(element["class"]):
            return str(element)
        elif "warning" in " ".join(element["class"]):
            macro_type = "warning"
            symbol = ":::"
        elif "error" in " ".join(element["class"]):
            macro_type = "danger"
            symbol = ":::"
        elif "information" in " ".join(element["class"]):
            macro_type = "info"
            symbol = ":::"
        else:
            symbol = ""  # Confluence hat komische macros die nichts machen/nicht dargestellt werden

    md = f"\n{symbol}{macro_type}\n"
    content = extract_text_recursively(element)
    # Jede Zeile des Inhalts einrücken
    indented_content = "\n    ".join(content.splitlines())
    md += indented_content

    return md.strip() + f"\n{symbol}\n"
