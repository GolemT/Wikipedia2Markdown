"""MD Konvertierung Verarbeitung"""

import os
from bs4 import NavigableString, Tag
from modules.img_handling import replace_images
from modules.text_handling import formatting_to_md, headers_to_markdown, escape_html_tags
from modules.table_handling import table_to_md
from modules.link_handling import link_to_md
from modules.list_handling import list_to_md
from modules.blockquote_handling import blockquote_to_md
from modules.logger import global_logger as logger

element_to_markdown_converter = {
    "noscript": { logger.info("Skipped noscript Tag")},
    "style": { logger.info("Skipped style Tag")},
    "a": link_to_md,
    "ul": list_to_md,
    "ol": list_to_md,
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
    "table": table_to_md,
}


def convert_to_md(element, target_url):
    """
    Konvertiert eine mit BeautifulSoup geparste Wikipedia-Seite in Markdown.

    Args:
        element (Tag oder NavigableString): HTML-Inhalt von Wikipedia.
        target_url (str): URL der Wikipedia-Seite.

    Returns:
        str: Konvertierter Markdown-Inhalt.
    """
    markdown = ""

    try:
        logger.debug(element)
        if isinstance(element, Tag):
            converter = element_to_markdown_converter.get(element.name)
            if converter:
                logger.debug(f"Konvertiere Element: <{element.name}> mit {converter.__name__}")

                if converter == list_to_md:
                    conversion_result = converter(element, target_url)
                else:
                    conversion_result = converter(element)

                if conversion_result is not None:
                    markdown += conversion_result
                else:
                    logger.warning(f"Keine Konvertierung für Element: <{element.name}>. Fallback zu Kindern.")
                    for child in element.children:
                        markdown += convert_to_md(child, target_url)

            elif not element.children:
                logger.debug("Element doesnt have any children, getting text instead")
                text = element.get_text(strip=True)
                if text:
                    markdown += text

            elif "class" in element.attrs:
                class_list = " ".join(element["class"])
                logger.debug(f"Unbekanntes HTML-Element mit Klassen: {class_list}")

                if "toc" in class_list:
                    markdown += ""  # Handle List of Contents
                elif "mw-editsection" in class_list:
                    markdown += ""
                else:
                    for child in element.children:
                        markdown += convert_to_md(child, target_url)
            else:
                for child in element.children:
                    markdown += convert_to_md(child, target_url)

        elif isinstance(element, NavigableString):
            logger.debug("Element ist ein navigable String: " + element)
            markdown += element

        return markdown + "\n"

    except Exception as e:
        logger.error(f"Fehler bei der Konvertierung eines Elements: {str(e)}")
        return ""


def make_md(path, title, content, target_url):
    """
    Erstellt eine .md-Datei und füllt sie mit dem konvertierten Inhalt einer Wikipedia-Seite.

    Args:
        path (str): Dateipfad zum Speichern der Markdown-Datei.
        title (str): Titel der Wikipedia-Seite.
        content (str): Geparster HTML-Inhalt zur Konvertierung.
    """
    try:
        logger.info(f"Starte Konvertierung von '{title}' nach Markdown...")

        md = f"# {title}" + "\n\n" + convert_to_md(content, target_url)
        md_path = os.path.join(f"landing/{path}/", f"{path}.md")

        os.makedirs(os.path.dirname(md_path), exist_ok=True)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md)

        logger.info(f"Markdown-Datei erfolgreich gespeichert: {md_path}")

    except Exception as e:
        logger.error(f"Fehler beim Erstellen der Markdown-Datei: {str(e)}")
