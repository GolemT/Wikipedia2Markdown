"""Macro Handling"""

from bs4 import Tag, NavigableString
from modules.logger import logger  # Logger importieren


def extract_text_recursively(element, target_url):
    """
    Extract text from all child elements recursively, handling specific tags appropriately.

    Args:
        element (HTML element): A HTML element with the word "macro" in the class attribute
        target_url (str): URL needed for handling certain conversions

    Returns:
        str: Formatted Markdown content extracted from the element.
    """
    try:
        text = ""
        for child in element.children:
            match child:
                case NavigableString() as ns:
                    if ns.name == "code":
                        from modules.code_handling import code_to_md
                        text += " " + code_to_md(ns)
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
                            text += "\n" + list_to_md(tag, target_url)
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
                            text += extract_text_recursively(tag, target_url)
                case _:
                    text += extract_text_recursively(child, target_url)

        logger.debug(f"Extrahierter Text aus Makro: {text.strip()[:100]}...")  # Loggt nur einen Teil zur Übersicht
        return text
    except Exception as e:
        logger.error(f"Fehler beim Extrahieren von Makro-Text: {str(e)}")
        return ""


def macro_to_md(element, target_url):
    """
    Converts Confluence macro-styled elements to Markdown based on their class attributes.
    Handles specific macro types like warning, error, and info by prepending them with
    appropriate symbols and formatting the content with indentation.

    Args:
        element (HTML Element): A HTML element with the word "macro" in the class attribute
        target_url (str): URL needed for Gliffy warnings

    Returns:
        str: Macro converted to Markdown Syntax
    """
    try:
        if "class" not in element.attrs:
            logger.warning("Makro-Element ohne Klasse erkannt, wird ignoriert.")
            return ""

        class_list = " ".join(element["class"])
        logger.debug(f"Erkannte Makro-Klassen: {class_list}")

        symbol = ""
        macro_type = ""

        if "status-macro" in class_list:
            logger.info("Status-Makro erkannt, wird unverändert zurückgegeben.")
            return str(element)
        elif "warning" in class_list:
            macro_type = "warning"
            symbol = ":::"
        elif "error" in class_list:
            macro_type = "danger"
            symbol = ":::"
        elif "information" in class_list:
            macro_type = "info"
            symbol = ":::"
        else:
            logger.warning(f"Unbekanntes Makro erkannt: {class_list}, wird ignoriert.")
            return ""

        logger.info(f"Makro erkannt: {macro_type}, wird konvertiert...")

        md = f"\n{symbol}{macro_type}\n"
        content = extract_text_recursively(element, target_url)

        if not content.strip():
            logger.warning(f"Makro '{macro_type}' enthält keinen Inhalt.")
            return ""

        indented_content = "\n    ".join(content.splitlines())
        md += indented_content

        logger.info(f"Makro '{macro_type}' erfolgreich konvertiert.")
        return md.strip() + f"\n{symbol}\n"

    except Exception as e:
        logger.error(f"Fehler bei der Makro-Konvertierung: {str(e)}")
        return ""
