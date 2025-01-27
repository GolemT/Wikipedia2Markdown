import subprocess

sites = ["https://de.wikipedia.org/wiki/Liste_von_Katzenrassen"]

for element in sites:
    subprocess.run(
        [
            "python",
            "./script/convert_main.py",
            "-u",
            element,
        ]
    )
