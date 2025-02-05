"""Document Handling"""

import os
from urllib.parse import unquote
import requests
from modules.text_handling import clean_str


def clean_filename(filename):
    """
    Sanitizes the filename by decoding URL-encoded characters, removing query parameters,
    and replacing invalid filesystem characters with underscores.

    Args:
        filename (String): Filename containing special characters like $

    Returns:
        String: cleaned Filename without special characters
    """

    filename = unquote(filename)
    filename = filename.split("?")[0]
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, "_")
    parts = filename.split(".")
    parts[0:-1] = [".".join(parts[0:-1]).replace(".", "")]
    return ".".join(parts)


def get_documents(element, base_url, title):
    """
    Downloads documents linked from 'a' tags with class 'confluence-embedded-file'.
    Constructs full URLs, sanitizes filenames, creates necessary directories, and
    streams the download to handle large files efficiently.

    Args:
        element (HTML Element): Element of the embedded document
        base_url (String): base url to download documents from confluence
        title (String): title to save documents under correct path
    """

    for doc in element.find_all("a", class_="confluence-embedded-file"):
        href = doc.get("href")
        if href:
            # Ensure the URL is properly formed
            doc_url = (base_url + href) if "://" not in href else href

            doc_name = clean_filename(href.split("/")[-1])
            doc_path = os.path.join(f"landing/{title}/assets", doc_name)

            # Create directories if they don't exist
            os.makedirs(os.path.dirname(doc_path), exist_ok=True)

            # Stream the download to handle large files
            response = requests.get(doc_url, headers=header, timeout=6000, stream=True)
            if response.status_code == 200:
                with open(doc_path, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
            else:
                print("fail to get doc")


def replace_doc(element):
    """
    Generates a Markdown link for a document. It extracts the URL from the provided element,
    sanitizes it by removing any query parameters, derives the document name, and formats it
    into a Markdown link pointing to a local directory.

    Args:
        element (HTML Element): The element in the page that needs to be replaced

    Returns:
        String: Link syntax to download the document
    """
    url = element.attrs.get("href")
    if "?" in url:
        index = url.find("?")
        url = url[:index]
    doc_name = clean_str(url.split("/")[-1])  # Get the last bit of the URL as name
    directory = f"./assets/{doc_name}"
    md_doc = f" [{doc_name}]({directory})"

    return md_doc
