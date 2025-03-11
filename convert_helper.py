import subprocess

from script.modules.logger import global_logger

sites = [
    "https://de.wikipedia.org/wiki/Liste_von_Katzenrassen",
    "https://en.wikipedia.org/wiki/Sphynx_cat",
    "https://en.wikipedia.org/wiki/Tabby_cat"]

for element in sites:
    subprocess.run(
        [
            "python",
            "./script/convert_main.py",
            "-u",
            element,
            "-l",
            "DEBUG"
        ]
    )
