"""Code Handling"""

from bs4 import Tag, NavigableString


def code_to_md(element):
    """
    Converts an HTML element containing code into a formatted Markdown code block.
    Determines the code's language from the element's class, collects all text within
    the element, handles nested code tags, and returns the text as a Markdown-formatted
    code block with language-specific syntax highlighting if applicable.

    Args:
        element (Table element): Since every code element is surrounded by tables the code
        needs to be extracted

    Returns:
        String: Markdown Syntax of code
    """
    # Sprache des Codes bestimmen, basierend auf den Klassenattributen des Elements
    language = ""
    if "powershell" in str(element):
        language = "powershell"

    # Sammle alle Texte innerhalb des übergebenen Elements rekursiv
    def collect_texts(elem):
        texts = []
        for item in elem.children:
            if isinstance(item, NavigableString):
                texts.append(item.strip())
            elif isinstance(item, Tag):
                if item.name == "code":
                    # Jede Zeile von Code wird individuell behandelt
                    texts.append(item.get_text())
                else:
                    # Rekursiv für alle anderen Tags
                    texts.extend(collect_texts(item))
        return texts

    code_texts = collect_texts(element)
    code_text = "\n".join(code_texts)

    # Formatierung in Markdown Code-Block
    if language:
        return f"\n```{language}\n{code_text.strip()}\n```\n"
    else:
        return f"\n```\n{code_text.strip()}\n```\n"
