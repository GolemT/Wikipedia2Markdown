"""URL Handling"""

import urllib.parse


def url_check(element):
    """
    Ensure proper URL formatting. If the URL already contains a query ("?"), it returns as is.
    Otherwise, it encodes the final segment after the last slash to handle special characters,
    reconstructing the full URL with the encoded segment.

    Args:
        element (String): Source of a HTML element that may contain a api request

    Returns:
        String: Source URL without the api request
    """
    if "?" in str(element):
        full_url = element
    else:
        first_half = element[0 : element.rfind("/") :]
        parsed_url = urllib.parse.quote(element.split("/")[-1])
        full_url = f"{first_half}/{parsed_url}"

    return full_url
