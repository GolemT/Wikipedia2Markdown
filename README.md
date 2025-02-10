# Wikipedia2Markdown

## Erläuterung

Wikipedia2Markdown ist ein Python Script welches eine Wikipedia Seite scannt und eine Markdown Datei (.md) mit den Inhalten anfertigt. Somit soll der Wechsel von Wikipedia zu einer anderen Dokumentation wie beispielsweise GitLab Pages vereinfacht werden.

## Ausführen des Skripts

### Setup

#### Dependencies

Um die benötigten python libraries zu installieren den folgenden Befehl in einen Terminal eingeben:

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

### Markdown Syntax

Hier is eine kurze Ansammlung an Markdown Syntax und schreibweisen.

# Heading 1
Heading 1
=========
## Heading 2
Heading 2
---------
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

:::warning Überschrift
Warning Message 
(Nur sichtbar in Browser, nicht in VS Code Preview)
:::

:::danger Überschrift
Danger Message 
(Nur sichtbar in Browser, nicht in VS Code Preview)
:::

:::info Überschrift
Info Message 
(Nur sichtbar in Browser, nicht in VS Code Preview)
:::

* Aufzählung
  * Eingerückte Aufzählung
  * Eingerückte Aufzählung
* Aufzählung
  1. Eingerückte Nummerierung
  2. Eingerückte Nummerierung
* Aufzählung

1. Nummerierte Aufzählung
    1. Eingerückte Nummerierung
    2. Eingerückte Nummerierung
2. Nummerierte Aufzählung
   * Eingerückte Aufzählung
   * Eingerückte Aufzählung
3. Nummerierte Aufzählung

```python
Code Block
```

```Code Snippet```

> Zitat:
>> Lorem ipsum dolor sit amet,
>>
>> consectetur adipisici elit
>
> — Docusaurus

| Table Header 1                 | Table Header 2                              |
| ----------------------- | ---------------------------------------- |
| Table Cell 1        | Table Cell 2  |
| X        | X  |

**Bold Text**

[Link](https://git.tech.rz.db.de/TimKosleck/Wikipedia2markdown)

### Image

![Image](./static/img/DB_rgb.png)

Separator line
---


## Probleme

Die Folgenden Problem bzw. Funktionalitäten konnten leider nicht umgesetzt werden. Dies hängt teils auch mit der späteren Implementierung in [Docusaurus](https://docusaurus.io/) zusammen.

* **Farbiger Text/Farbige Tabellen**
  * In der Wikipedia Seite werden für bestimmte Farben so wie spezifische Größen Style-elemente benutzt. Wenn diese einfach importiert werden schimpft docusaurus das wir jsx styling benutzen sollen. Wenn wir allerdings das styling händisch in jsx umwandeln, kriegen wir eine Fehlermeldung das ein Character namens "acorn" nicht verarbeitet werden kann. Somit ist unklar welches styling wirklich gebraucht wird und eine Formatierung nicht möglich
* **Checkboxen/TODO**
  * Im normalen MD gibt es keine Checkboxen. In Versionen wo dies funktioniert wurde md um einige Funktionen erweitert (Beispiel git flavoured md). Um das Umzusetzten müsste man seine eigene MD Erweiterung schreiben
* **Formatierung**
  * Es ließen sich keine klaren Regeln für Formatierungen finden, weshalb manche Pages ein paar Umbrüche zu viel haben. Ursache davon ist die unterschiedliche Struktur der HTML page von Wikipedia.
