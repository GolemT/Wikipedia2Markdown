import subprocess

sites = [
    "https://cdp.jaas.service.deutschebahn.com/confluence/display/dmp/Azure+Consumption+API+abfragen"
]

for element in sites:
    subprocess.run(
        [
            "python",
            "./script/convert_main.py",
            "-u",
            element,
        ]
    )
