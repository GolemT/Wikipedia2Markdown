"""Image Handling"""

import os
import requests
from script.modules.text_handling import clean_str, formatting_to_md

classes = ["avatar", "gliffy", "emoticons", "userLogo "]


def check_class(element):
    """
    Checks if any predefined class names are present in the 'class' attribute of the given element.
    Returns True if a matching class is found, otherwise False.

    Args:
        element (img element): img element to be checked

    Returns:
        boolean: wether certain classes are within the element or not
    """
    if element.attrs.get("class"):
        for item in classes:
            if item in str(element.attrs.get("class")):
                return True

    else:
        return False


def get_images(element, base_url, title):
    """
    Retrieves and downloads all images from a given HTML element, excluding those
    with specific classes. Images are saved to a designated assets directory, and
    filenames are sanitized and stripped of query parameters.

    Args:
        element (img element): An img element found in the Confluence page
        base_url (String): Url to download pictures form Confluence
        title (String): Filename to save pictures to the correct folder
    """

    for image in element.find_all("img"):

        if not check_class(image):

            if "://" not in str(image.attrs.get("src")):
                img_url = "https:" + str(image.attrs.get("src"))
            else:
                img_url = str(image.attrs.get("src"))

            if "?" in img_url:
                # print("fiuwar") # Found Image Url With Api Request:)
                index = img_url.find("?")
                img_url = img_url[:index]

            img_data = requests.get(img_url, timeout=6000).content
            img_name = clean_str(
                img_url.split("/")[-1]
            )  # Get the last bit of the URL as name
            if len(img_name) > 15:
                img_name = img_name[:15] + img_name[-4:]
            img_path = os.path.join(f"landing/{title}/assets/", img_name)

            print(img_url)
            print(img_path)
            print(img_name)

            with open(img_path, "wb") as f:
                f.write(img_data)


def replace_images(element):
    """
    Processes an image element to create a Markdown image link. Strips query parameters
    from the URL, sanitizes the filename, and handles any nested textual elements as
    captions or additional descriptions.

    Args:
        element (img element): The image element that needs to be converted

    Returns:
        String: Markdown Syntax of images
    """
    url = element.attrs.get("src")
    if "?" in url:
        index = url.find("?")
        url = url[:index]
    img_name = clean_str(url.split("/")[-1])  # Get the last bit of the URL as name
    directory = f"./assets/{img_name}"
    md_img = f" ![{img_name}]({directory})"

    # Some Image Elements have other HTML Elements as Children
    text = ""
    if element.children:
        for child in element.children:
            if child.name in ["strong", "em", "s", "u"]:
                text += formatting_to_md(child)
            else:
                text += child.get_text()

    full_img = md_img + text

    return full_img
