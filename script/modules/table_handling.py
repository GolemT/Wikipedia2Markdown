"""Table Handling"""

from bs4 import BeautifulSoup, NavigableString
from modules.img_handling import replace_images
from modules.link_handling import link_to_md
from modules.link_handling import jira_to_md
from modules.gliffy_handling import gliffy_warning


@staticmethod
def table_to_md(table, target_url):
    """
    Processes a BeautifulSoup table element to remove styles,
    handle specific tags like images and breaks, and replace
    certain elements with their markdown equivalents. Cleans
    up the table HTML by removing styles, converting images,
    links, and nested tables, and flattening JIRA issues and
    text nodes.

    Args:
        table (table element): table that needs to be converted
        target_url (String): URL to be converted for gliffy warnings

    Returns:
        String: single line string representation of the modified table.
    """

    if table and "style" in table.attrs:
        del table["style"]

    to_process = table.find_all(True)  # Find all tags beneath the table

    for element in to_process:
        if element.has_attr("style"):
            del element["style"]

        if element.name == "img":
            element.replace_with(replace_images(element))
        elif element.name == "br":
            element.decompose()
        elif element.name == "table":
            table_text = table_to_md(element, target_url)
            inner_table = BeautifulSoup(table_text, "html.parser")
            element.replace_with(inner_table)
        elif element.name == "a":
            element.replace_with(link_to_md(element))
        elif "class" in element.attrs and "jira-issue" in " ".join(element["class"]):
            element.replace_with(jira_to_md(element))
        elif "class" in element.attrs and "gliffy-container" in " ".join(
            element["class"]
        ):
            element.replace_with(gliffy_warning(target_url))
        elif isinstance(element, NavigableString):
            cleaned_text = " ".join(element.string.split())
            element.replace_with(cleaned_text)

    final_table = "".join(str(table).splitlines())

    return final_table
