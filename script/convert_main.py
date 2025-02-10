"""
Script File to Convert a Wikipedia Page into Markdown
so that it can be used in a docusaurus implementation
"""


import os
import argparse
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from modules.img_handling import get_images
from modules.md_convert import make_md
from modules.url_handling import url_check
from modules.text_handling import clean_str
from modules.logger import global_logger as logger

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", required=True, help="The Wikipedia url of the page that should be converted")
parser.add_argument("-l", "--log", required=False, help="Setzt das Log-Level (DEBUG, INFO, WARNING, ERROR)")
arg = parser.parse_args()

if arg.log:
    logger.set_level(arg.log.upper())  # Ändert das Log-Level von der CLI aus

target_url = url_check(str(arg.url))
base_url = f"{urlparse(target_url).scheme}://{urlparse(target_url).netloc}"
title = ""
path = ""

logger.info(f"Starte die Konvertierung für: {target_url}")

# HTML abrufen
try:
    response = requests.get(target_url, timeout=6000)
    response.raise_for_status()  # Falls die Seite nicht geladen werden kann
    logger.info("HTML erfolgreich abgerufen.")
except requests.exceptions.RequestException as e:
    logger.error(f"Fehler beim Abrufen der Seite: {str(e)}")
    exit(1)  # Beende das Skript, wenn die Seite nicht geladen werden kann


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
    parses it into a BeautifulSoup object.
    """
    try:
        soup = BeautifulSoup(response.content, "html.parser")
        global title
        title = str(soup.find("h1").get_text(strip=True))
        global path
        path = clean_str(title).replace(".", "")
        path = truncate_string(path)

        logger.info(f"Seiten-Titel erkannt: {title}")
        logger.info(f"Pfad für Speicherung: {path}")

        os.makedirs(f"landing/{path}/assets", exist_ok=True)
        logger.info(f"Ordnerstruktur erstellt: landing/{path}/assets")

        return soup.find("div", id="bodyContent")
    except Exception as e:
        logger.error(f"Fehler beim Parsen der HTML-Seite: {str(e)}")
        return None

try:
    # run conversion
    content = url_to_html()
    logger.info("Recieved HTML content")
    get_images(content, path)
    logger.info("Finished Downloading Images")
    make_md(path, title, content, target_url)
    logger.info("Konvertierung erfolgreich abgeschlossen! 🚀")
    exit(0)
except Exception as e:
    logger.error(f"Fehler beim Konvertieren der Seite: {e}")
finally:
    logger.shutdown()


