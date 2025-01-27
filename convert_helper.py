import subprocess

sites = ["https://de.wikipedia.org/wiki/Formel_1"]

for element in sites:
    subprocess.run(
        [
            "python",
            "./script/convert_main.py",
            "-u",
            element,
        ]
    )
