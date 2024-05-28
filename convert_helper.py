import subprocess

sites = [""]

for element in sites:
    subprocess.run(
        [
            "python",
            "./script/convert_main.py",
            "-u",
            element,
        ]
    )
