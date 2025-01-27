"""MD Convert Handling"""

import os
from bs4 import NavigableString, Tag
from script.modules.img_handling import replace_images
from script.modules.text_handling import formatting_to_md, headers_to_markdown
from script.modules.table_handling import table_to_md
from script.modules.link_handling import link_to_md
from script.modules.link_handling import jira_to_md
from script.modules.list_handling import list_to_md
from script.modules.code_handling import code_to_md
from script.modules.gliffy_handling import gliffy_warning
from script.modules.macro_handling import macro_to_md
from script.modules.blockquote_handling import blockquote_to_md

element_to_markdown_converter = {
    "a": link_to_md,
    "code": code_to_md,
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
}


def convert_to_md(element, target_url):
    """
    Take a Confluence Page parsed with bs4 and convert each element into Markdown

    Args:
        element (div element): Main Content of the Confluence page from which every element is read
        target_url (String): URL to be converted for gliffy warnings

    Returns:
        String: A complete String with every element of the confluence page
    """
    markdown = ""

    if isinstance(element, Tag):
        converter = element_to_markdown_converter.get(element.name)
        if converter:
            # The list function needs 2 Arguments instead of 1
            if converter == list_to_md:
                conversion_result = converter(element, target_url)
            else:
                conversion_result = converter(element)
            if conversion_result is not None:
                markdown += conversion_result
            else:
                if element.find(True):  # If there are other HTML children
                    for child in element.children:
                        markdown += convert_to_md(child, target_url)

        elif (
            not element.children
        ):  # If there are no other Tag Children simply get the text from the element
            text = element.get_text(strip=True)
            if text:
                markdown += text
        elif element.name == "table":
            markdown += table_to_md(element, target_url)

        # If no Converter function is available, handle specific cases and search the children
        elif (
            not converter and element.children
        ):  # Wenn Kinder existieren, die Tags sind
            if "class" in element.attrs and "gliffy-container" in " ".join(
                element["class"]
            ):
                markdown += gliffy_warning(target_url)
            elif "class" in element.attrs and "code" in " ".join(element["class"]):
                markdown += code_to_md(element)
            elif (
                "class" in element.attrs
                and "macro" in " ".join(element["class"])
                and not "table" in " ".join(element["class"])
            ):
                markdown += "\n" + macro_to_md(element, target_url)
            elif "class" in element.attrs and "jira-issue" in " ".join(
                element["class"]
            ):
                markdown += jira_to_md(element)
            else:
                for child in element.children:
                    markdown += convert_to_md(child, target_url)
    elif isinstance(element, NavigableString):
        text = element.strip()
        text = escape_html_tags(text)
        if text:
            # Add the text of the NavigableString
            markdown += text

    return markdown + "\n"


def make_md(path, title, content, target_url):
    """
    Function to create a .md file and populate it with the content of the given confluence page

    Args:
        path (String): filepath showing where to save the converted .md file
        title (String): title of the confluence page to name the .md file
        content (String): div that hold every element that needs to be converted
        target_url (String): URL to be converted for gliffy warnings
    """
    md = f"# {title}" + "\n\n" + convert_to_md(content, target_url)
    md_path = os.path.join(f"landing/{path}/", f"{path}.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)
