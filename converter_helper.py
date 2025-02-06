import subprocess

from script.modules.logger import global_logger

sites = ["https://de.wikipedia.org/wiki/Liste_von_Katzenrassen"]

for element in sites:
    subprocess.run(
        [
            "python",
            "./script/convert_main.py",
            "-u",
            element,
            "-l",
            "WARNING"
        ]
    )
