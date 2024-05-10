"""
Defines the header for requests to authenticate the user against the confluence page
"""

import os
from dotenv import load_dotenv

load_dotenv()


def get_header():
    TOKEN = str(os.environ.get("CONFLUENCE_TOKEN"))

    if TOKEN == "None":
        raise ValueError(
            "Confluence Token wasn't defined in the environment. Look at the documentation for more information"
        )
    header = {"Authorization": "Bearer " + TOKEN}
    return header
