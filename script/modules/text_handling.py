"""Text Handling"""

import re
from bs4 import Tag
from modules.logger import global_logger as logger


def headers_to_markdown(element):
    """
    Converts HTML header elements (h1 to h6) to their equivalent Markdown format.

    Args:
        element (Tag): HTML header element.

    Returns:
        String | None: Markdown header or None if not processable.
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
    Converts HTML formatting elements (s, strong, u, em) to their Markdown or HTML equivalents.

    Args:
        element (Tag): HTML element with formatted text.

    Returns:
        String: Markdown formatted text.
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
    Cleans a string by removing special characters and replacing spaces with underscores.

    Args:
        element (str): Input string with special characters.

    Returns:
        str: Cleaned string.
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
    Escapes HTML tags by replacing '<' and '>' with their HTML entities.

    Args:
        text (str): Text containing HTML elements.

    Returns:
        str: Escaped text.
    """
    try:
        wip_text = re.sub(r"<", "&lt;", text)
        wip_text = re.sub(r">", "&gt;", wip_text)
        logger.debug(f"HTML-Tags escaped: {wip_text}")
        return wip_text

    except Exception as e:
        logger.error(f"Fehler beim Escapen von HTML-Tags: {str(e)}")
        return text
