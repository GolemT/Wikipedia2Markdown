"""Bildverarbeitung"""

import os
import requests
from modules.logger import global_logger as logger
from modules.text_handling import clean_str, formatting_to_md

classes = ["avatar", "emoticons"]


def check_class(element):
    """
    Überprüft, ob vordefinierte Klassennamen im 'class'-Attribut des gegebenen Elements vorhanden sind.
    Gibt True zurück, wenn eine übereinstimmende Klasse gefunden wird, andernfalls False.

    Args:
        element (Tag): Zu überprüfendes img-Element.

    Returns:
        bool: Ob bestimmte Klassen im Element enthalten sind oder nicht.
    """
    if element.attrs.get("class"):
        for item in classes:
            if item in str(element.attrs.get("class")):
                logger.debug(f"Bild ignoriert wegen Klasse: {item}")
                return True
    return False


def get_images(element, title):
    """
    Ruft alle Bilder von einem gegebenen HTML-Element ab und lädt sie herunter, mit Ausnahme derer
    mit bestimmten Klassen. Bilder werden in einem bestimmten Assets-Verzeichnis gespeichert, und
    Dateinamen werden bereinigt und von Abfrageparametern befreit.

    Args:
        element (Tag): Ein in der Wikipedia-Seite gefundenes img-Element.
        title (str): Dateiname, um Bilder im richtigen Ordner zu speichern.
    """
    try:
        image_tags = element.find_all("img")
        if not image_tags:
            logger.warning("Keine Bilder zum Herunterladen gefunden.")
            return

        os.makedirs(f"landing/{title}/assets/", exist_ok=True)
        logger.info(f"Speicherort für Bilder: landing/{title}/assets/")

        for image in image_tags:
            if not check_class(image):
                img_url = image.attrs.get("src", "")

                if "://" not in img_url:
                    img_url = "https:" + img_url

                if "?" in img_url:
                    img_url = img_url.split("?")[0]  # Entferne Query-Parameter

                try:
                    logger.debug(f"Lade Bild herunter: {img_url}")
                    img_data = requests.get(img_url, timeout=6000).content
                    img_name = clean_str(img_url.split("/")[-1])  # Verwende letzten Teil der URL als Namen
                    if len(img_name) > 15:
                        img_name = img_name[:15] + img_name[-4:]  # Begrenze Länge des Namens
                    img_path = os.path.join(f"landing/{title}/assets/", img_name)

                    with open(img_path, "wb") as f:
                        f.write(img_data)

                    logger.info(f"Bild gespeichert: {img_path}")

                except requests.RequestException as e:
                    logger.error(f"Fehler beim Herunterladen von {img_url}: {str(e)}")

    except Exception as e:
        logger.error(f"Fehler beim Verarbeiten von Bildern: {str(e)}")


def replace_images(element):
    """
    Verarbeitet ein Bildelement, um einen Markdown-Bildlink zu erstellen. Entfernt Abfrageparameter
    aus der URL, bereinigt den Dateinamen und behandelt alle verschachtelten Textelemente als
    Beschriftungen oder zusätzliche Beschreibungen.

    Args:
        element (Tag): Das zu konvertierende Bildelement.

    Returns:
        str: Markdown-Syntax von Bildern.
    """
    try:
        url = element.attrs.get("src", "")
        if "?" in url:
            url = url.split("?")[0]

        img_name = clean_str(url.split("/")[-1])
        if len(img_name) > 15: # Begrenze Länge des Namens damit diese im MD mit den Assets übereinstimmen
            img_name = img_name[:15] + img_name[-4:]
        directory = f"./assets/{img_name}"
        md_img = f"![{img_name}]({directory})"

        text = " "
        if element.children:
            for child in element.children:
                if child.name in ["strong", "em", "s", "u"]:
                    text += formatting_to_md(child)
                else:
                    text += child.get_text()

        full_img = md_img + text

        logger.info(f"Markdown-Bild erfolgreich generiert: {full_img.strip()}")
        return full_img

    except Exception as e:
        logger.error(f"Fehler bei der Bild-Konvertierung zu Markdown: {str(e)}")
        return ""
