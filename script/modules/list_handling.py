"""Listenverarbeitung"""

from bs4 import NavigableString, Tag
from modules.logger import global_logger as logger
from modules.text_handling import (
    formatting_to_md,
    headers_to_markdown,
    escape_html_tags,
)
from modules.img_handling import replace_images
from modules.link_handling import link_to_md
from modules.blockquote_handling import blockquote_to_md
from modules.table_handling import table_to_md


def list_to_md(input, target_url, ebene=0):
    """
    Konvertiert ein ungeordnetes Listenelement auf der Wikipedia-Seite in Markdown.

    Args:
        input (Tag): Das zu konvertierende Listenelement.
        target_url (str): Die Ziel-URL zur Behandlung spezieller Elemente.
        ebene (int, optional): Tiefe der Liste (wird zur Einrückung verwendet). Standardmäßig 0.

    Returns:
        str: Markdown-Syntax für ungeordnete Listen.
    """
    try:
        if input.name == "ol":
            return ordered_list_to_md(input, target_url, ebene)

        logger.debug(f"Konvertiere ungeordnete Liste auf Ebene {ebene}...")

        liste = ""
        einrueckung = "  " * ebene  # Leerzeichen für die Einrückung

        for element in input.find_all(recursive=False):
            item = search_child(element, target_url, ebene)
            if element.name != "li":
                liste += f"{einrueckung} {item}\n"
            else:
                liste += f"{einrueckung}* {item}\n"

        logger.info(f"Ungeordnete Liste erfolgreich konvertiert (Ebene {ebene})")
        return liste

    except Exception as e:
        logger.error(f"Fehler bei der Konvertierung einer ungeordneten Liste: {str(e)}")
        return ""


def ordered_list_to_md(input, target_url, depth):
    """
    Konvertiert ein geordnetes Listenelement auf der Wikipedia-Seite in Markdown.

    Args:
        input (Tag): Das geordnete Listenelement.
        target_url (str): Die Ziel-URL zur Behandlung spezieller Elemente.
        depth (int): Tiefe der Liste zur Einrückung.

    Returns:
        str: Markdown-Syntax für geordnete Listen.
    """
    try:
        logger.debug(f"Konvertiere geordnete Liste auf Ebene {depth}...")

        liste = ""
        einrueckung = "   " * depth  # Leerzeichen für die Einrückung
        number = 1

        for element in input.find_all(recursive=False):
            item = search_child(element, target_url, depth)
            if element.name != "li":
                liste += f"{einrueckung} {item}\n"
            else:
                liste += f"{einrueckung}{number}. {item}\n"
                number += 1

        logger.info(f"Geordnete Liste erfolgreich konvertiert (Ebene {depth})")
        return liste

    except Exception as e:
        logger.error(f"Fehler bei der Konvertierung einer geordneten Liste: {str(e)}")
        return ""


def search_child(element, target_url, depth=0):
    """
    Durchsucht rekursiv ein Element und konvertiert es in Markdown.

    Args:
        element (Tag | NavigableString): Das zu konvertierende Element.
        target_url (str): Die Ziel-URL zur Behandlung spezieller Elemente.
        depth (int, optional): Aktuelle Rekursionstiefe. Standardmäßig 0.

    Returns:
        str: Konvertierter Markdown-String.
    """
    try:
        element_to_markdown_converter = {
            "a": link_to_md,
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
            if element.name == "style":  # Style elemente wurden teilweise in referenzen mit Eingebunden
                return ""
            if "class" in element.attrs:
                classes = set(element.attrs[
                                  "class"])  # cs1 sind irgendwelche Kommentare, die aber in Wikipedia selber nicht sichtbar sind. Deswegen werden die explizit rausgeworfen.
                if classes.issubset({"cs1-maint citation-comment", "cs1-code"}):
                    return ""

            converter = element_to_markdown_converter.get(element.name)
            if converter:
                logger.debug(f"Konvertiere Element: <{element.name}> in einer Liste.")
                conversion_result = converter(element)
                if conversion_result is not None:
                    markdown += conversion_result
            elif not element.children:
                text = element.get_text(strip=True)
                if text:
                    markdown += text
            elif element.name == "table":
                logger.info("Tabelle in einer Liste gefunden, wird konvertiert...")
                markdown += table_to_md(element)
            elif element.name == "ul":
                logger.debug("Ungeordnete Liste in einer Liste erkannt, wird rekursiv konvertiert...")
                markdown += "\n" + list_to_md(element, target_url, depth + 1)
            elif element.name == "ol":
                logger.debug("Geordnete Liste in einer Liste erkannt, wird rekursiv konvertiert...")
                markdown += "\n" + ordered_list_to_md(element, target_url, depth + 1)
            elif not converter and element.children:
                for child in element.children:
                    markdown += search_child(child, target_url, depth)

        elif isinstance(element, NavigableString):
            text = element.strip()
            text = escape_html_tags(text)
            if text:
                markdown += text

        return markdown

    except Exception as e:
        logger.error(f"Fehler beim Verarbeiten eines Listenelements: {str(e)}")
        return ""
