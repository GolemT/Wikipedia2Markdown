"""Code Handling"""

from bs4 import Tag, NavigableString
from modules.logger import logger  # Logger importieren


def code_to_md(element):
    """
    Converts an HTML element containing code into a formatted Markdown code block.

    Args:
        element (Tag): HTML element that contains the code.

    Returns:
        str: Markdown-formatted code block.
    """
    try:
        if element is None:
            logger.warning("Kein gültiges Code-Element übergeben, wird ignoriert.")
            return ""

        logger.debug("Starte Code-Konvertierung...")

        # Sprache des Codes bestimmen, basierend auf den Klassenattributen des Elements
        language = ""
        class_list = element.get("class", [])
        if any("powershell" in c.lower() for c in class_list):
            language = "powershell"

        if language:
            logger.info(f"Erkannte Programmiersprache: {language}")
        else:
            logger.warning("Keine Programmiersprache erkannt, Markdown wird ohne Highlighting erstellt.")

        # Rekursive Funktion zum Sammeln aller Texte innerhalb des Elements
        def collect_texts(elem):
            texts = []
            for item in elem.children:
                if isinstance(item, NavigableString):
                    texts.append(item.strip())
                elif isinstance(item, Tag):
                    if item.name == "code":
                        texts.append(item.get_text())
                    else:
                        texts.extend(collect_texts(item))
            return texts

        code_texts = collect_texts(element)
        code_text = "\n".join(code_texts).strip()

        # Formatierung in Markdown Code-Block
        md_code_block = f"\n```{language}\n{code_text}\n```\n" if language else f"\n```\n{code_text}\n```\n"

        logger.info(f"Codeblock erfolgreich konvertiert:\n{md_code_block[:100]}...")  # Loggt nur einen Ausschnitt
        return md_code_block

    except Exception as e:
        logger.error(f"Fehler bei der Code-Konvertierung: {str(e)}")
        return ""
