"""Textverarbeitung"""

import re
from bs4 import Tag
from modules.logger import global_logger as logger


def headers_to_markdown(element):
    """
    Konvertiert HTML-Überschriftenelemente (h1 bis h6) in ihr äquivalentes Markdown-Format.

    Args:
        element (Tag): HTML-Überschriftenelement.

    Returns:
        String | None: Markdown-Überschrift oder None, wenn nicht verarbeitbar.
    """
    try:
        if element.name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            logger.debug(f"Konvertiere Header: <{element.name}>")

            if any(isinstance(child, Tag) for child in element.children):
                logger.warning(f"Header enthält geschachtelte Tags und wird ignoriert: <{element.name}>")
                return None

            if element.get_text(strip=True):
                level = int(element.name[1])
                text = formatting_to_md(element).strip()
                headertype = "#" * level
                markdown_header = headertype + " " + text + "\n"

                logger.info(f"Header konvertiert: {markdown_header.strip()}")
                return markdown_header

        return None

    except Exception as e:
        logger.error(f"Fehler bei der Header-Konvertierung: {str(e)}")
        return None


def formatting_to_md(element):
    """
    Konvertiert HTML-Formatierungselemente (s, strong, u, em) in ihre Markdown- oder HTML-Äquivalente.

    Args:
        element (Tag): HTML-Element mit formatiertem Text.

    Returns:
        String: Markdown-formatierter Text.
    """
    try:
        format_symbol = ""
        if element.name == "s":
            format_symbol = "~~"
        elif element.name == "strong":
            format_symbol = "**"
        elif element.name == "u":
            format_symbol = "<u>"
        elif element.name == "em":
            format_symbol = "_"

        logger.debug(f"Formatierung erkannt: <{element.name}> mit Symbol {format_symbol}")

        formatted_text = format_symbol
        for child in element.children:
            if isinstance(child, Tag):
                formatted_text += formatting_to_md(child)
            else:
                formatted_text += escape_html_tags(child.string.strip())
        formatted_text += format_symbol[::-1].replace(">u<", "</u>")

        logger.info(f"Text formatiert: {formatted_text}")
        return formatted_text.strip()

    except Exception as e:
        logger.error(f"Fehler bei der Textformatierung: {str(e)}")
        return element.get_text(strip=True) if element else ""


def clean_str(element):
    """
    Bereinigt einen String, indem Sonderzeichen entfernt und Leerzeichen durch Unterstriche ersetzt werden.

    Args:
        element (str): Eingabe-String mit Sonderzeichen.

    Returns:
        str: Bereinigter String.
    """
    try:
        regex_pattern = r"[^a-zA-Z0-9\s\.]"
        cleaned_string = re.sub(regex_pattern, " ", element).strip().replace(" ", "_")
        logger.info(f"String bereinigt: {cleaned_string}")
        return escape_html_tags(cleaned_string)

    except Exception as e:
        logger.error(f"Fehler beim Bereinigen des Strings: {str(e)}")
        return element


def escape_html_tags(text):
    """
    Maskiert HTML-Tags, indem '<' und '>' durch ihre HTML-Entities ersetzt werden.

    Args:
        text (str): Text mit HTML-Elementen.

    Returns:
        str: Maskierter Text.
    """
    try:
        wip_text = re.sub(r"<", "&lt;", text)
        wip_text = re.sub(r">", "&gt;", wip_text)
        logger.debug(f"HTML-Tags escaped: {wip_text}")
        return wip_text

    except Exception as e:
        logger.error(f"Fehler beim Escapen von HTML-Tags: {str(e)}")
        return text
