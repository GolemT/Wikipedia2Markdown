---
sidebar_position: 1
---

# Wikipedia2Markdown

## Erläuterung

Wikipedia2Markdown ist ein Python Script welches eine Wikipedia Seite scannt und eine Markdown Datei (.md) mit den Inhalten anfertigt. Somit soll der Wechsel von Wikipedia zu einer anderen Dokumentation wie beispielsweise GitLab Pages vereinfacht werden.

## Ausführen des Skripts

### Setup

#### Dependencies

Um die benötigten python libraries zu installieren, den folgenden Befehl in einen Terminal eingeben:

```Powershell
    pip install bs4 requests dotenv
```

Alternativ kann mit der ```requirements.txt``` eine virtuelle Python Umgebung [venv](https://docs.python.org/3/library/venv.html) erstellt werden.

### Nutzung

Zur Nutzung des Script muss die zu konvertierende Seite in Wikipedia angegeben werden. Dies wird beim ausfuehren des Scripts mit der Flag -u angehängt.

Alternativ kann das Script ```convert_helper.py``` genutzt werden. Dieses Script nimmt ein Array an Links und arbeitet dieses ab. Dadurch müssen die URLs nicht einzeln konvertiert werden.

Bsp:

```bash
  python /path/to/convert_main.py -u https://domain.com/Wikipedia_subpage
```

oder:

```bash
  python /path/to/convert_helper-py
```

Nach dem Einsetzen der gewünschten URL kann das Script ausgeführt werden. Das Ergebnis wird als Ordnerstruktur mit allen Assets unter landing/ angelegt. Von dort aus kann der Ordner an den gewünschten Ort verschoben werden.

## Docusaurus

### Install

```bash
npm i
```

### Running

```bash
npm start
```

## Technologie

Die Markdown Dateien verwenden MDX, weshalb sie in der Lage sind HTML Elemente anzuzeigen. Ursprünglich wurde dieses Skript genutzt, um Wikipedia Seiten in einer durch [Docusaurus](https://docusaurus.io/) generierten Dokumentation anzuzeigen. Daher werden bestimmte JSX Elemente in der Markdown verwendet.