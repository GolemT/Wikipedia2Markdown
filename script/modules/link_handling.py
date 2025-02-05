"""Link Handling"""

from modules.doc_handling import replace_doc
from modules.img_handling import replace_images


def link_to_md(element):
    """
    Converts an HTML anchor element into a Markdown link.

    Args:
        element (a element): A Link on the Wiki page

    Returns:
        String: Markdown Syntax for Links
    """

    md_link = ""
    
    text = element.get_text(strip=True)
    if element.get("href", ""):
        url = element.get("href", "")
    else:
        url = "nolink"
        
    if url.startswith("/wiki/"):
        url = f"https://de.wikipedia.org{url}"
    md_link = f"[{text}]({url})"

    return md_link
