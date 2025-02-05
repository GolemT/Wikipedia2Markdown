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
        filename (str): Filename containing special characters like $

    Returns:
        str: Cleaned filename without special characters.
    """
    try:
        filename = unquote(filename).split("?")[0]
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            filename = filename.replace(char, "_")
        parts = filename.split(".")
        parts[0:-1] = [".".join(parts[0:-1]).replace(".", "")]
        logger.debug(f"Bereinigter Dateiname: {filename}")
        return ".".join(parts)
    except Exception as e:
        logger.error(f"Fehler beim Bereinigen des Dateinamens: {str(e)}")
        return "unknown_file"


def get_documents(element, base_url, title):
    """
    Downloads documents linked from 'a' tags with class 'confluence-embedded-file'.
    Constructs full URLs, sanitizes filenames, creates necessary directories, and
    streams the download to handle large files efficiently.

    Args:
        element (Tag): Element of the embedded document.
        base_url (str): Base URL to download documents from Confluence.
        title (str): Title to save documents under correct path.
    """
    try:
        document_links = element.find_all("a", class_="confluence-embedded-file")
        if not document_links:
            logger.warning("Keine Dokumente zum Herunterladen gefunden.")
            return

        os.makedirs(f"landing/{title}/assets/", exist_ok=True)
        logger.info(f"Speicherort für Dokumente: landing/{title}/assets/")

        for doc in document_links:
            href = doc.get("href")
            if not href:
                logger.warning("Dokument enthält keine gültige URL, wird übersprungen.")
                continue

            doc_url = base_url + href if "://" not in href else href
            doc_name = clean_filename(href.split("/")[-1])
            doc_path = os.path.join(f"landing/{title}/assets", doc_name)

            try:
                logger.debug(f"Lade Dokument herunter: {doc_url}")
                response = requests.get(doc_url, timeout=6000, stream=True)
                if response.status_code == 200:
                    with open(doc_path, "wb") as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    logger.info(f"Dokument erfolgreich gespeichert: {doc_path}")
                else:
                    logger.error(f"Fehler beim Abrufen von {doc_url}: HTTP {response.status_code}")

            except requests.RequestException as e:
                logger.error(f"Fehler beim Herunterladen von {doc_url}: {str(e)}")

    except Exception as e:
        logger.error(f"Fehler beim Verarbeiten von Dokumenten: {str(e)}")


def replace_doc(element):
    """
    Generates a Markdown link for a document. It extracts the URL from the provided element,
    sanitizes it by removing any query parameters, derives the document name, and formats it
    into a Markdown link pointing to a local directory.

    Args:
        element (Tag): The element in the page that needs to be replaced.

    Returns:
        str: Markdown link to the document.
    """
    try:
        url = element.attrs.get("href", "")
        if not url:
            logger.warning("Kein gültiger URL-Link für das Dokument gefunden.")
            return ""

        if "?" in url:
            url = url.split("?")[0]

        doc_name = clean_str(url.split("/")[-1])
        directory = f"./assets/{doc_name}"
        md_doc = f"[{doc_name}]({directory})"

        logger.info(f"Markdown-Link für Dokument erstellt: {md_doc}")
        return md_doc

    except Exception as e:
        logger.error(f"Fehler bei der Umwandlung eines Dokuments in Markdown: {str(e)}")
        return ""
