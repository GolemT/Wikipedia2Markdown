"""
Script File to Convert a Confluence Page into Markdown 
so that it can be used in a docusaurus implementation
"""

import os
import argparse
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from modules.auth import get_header
from modules.img_handling import get_images
from modules.md_convert import make_md
from modules.url_handling import url_check
from modules.text_handling import clean_str
from modules.doc_handling import get_documents

parser = argparse.ArgumentParser()
parser.add_argument(
    "-u",
    "--url",
    required=True,
    help="The Confluence url of the page that should be converted",
)
arg = parser.parse_args()
target_url = url_check(str(arg.url))
base_url = f"{urlparse(target_url).scheme}://{urlparse(target_url).netloc}"
title = ""
path = ""
header = get_header()

response = requests.get(target_url, headers=header, timeout=6000)


def truncate_string(string, max_length=50):
    """
    Truncate the input string to a specified maximum length.

    Args:
        string (str): The input string to be truncated.
        max_length (int): The maximum length of the truncated string.

    Returns:
        str: The truncated string.
    """
    if len(string) <= max_length:
        return string
    return string[:max_length].rstrip()


def url_to_html():
    """
    Fetches the HTML content of the target URL using requests and
    parses it into a BeautifulSoup object. It attempts to create
    a directory structure for storing the page assets based on the
    page title.

    Returns:
        bs4 element: BeautifulSoup object of the fetched HTML for further processing
    """
    soup = BeautifulSoup(response.content, "html.parser")
    global title
    title = str(
        soup.find("h1").get_text(strip=True)
    )  # The file should have the title only internally
    global path
    path = clean_str(str(soup.find("h1").get_text(strip=True))).replace(
        ".", ""
    )  # Path should not contain special characters
    path = truncate_string(path)  # Truncate path

    try:
        os.makedirs(f"landing/{path}/assets")
        return soup.find("div", id="main-content")
    except OSError as e:
        print("folder already exists")
        exit()


# run conversion
content = url_to_html()
get_images(content, base_url, path)
get_documents(content, base_url, path)
make_md(path, title, content, target_url)
