# Confluence2Markdown

## Erläuterung

Confluence2Markdown ist ein Python Script welches eine Confluence Seite scannt und eine Markdown Datei (.md) mit den Inhalten anfertigt. Somit soll der Wechsel von Confluence zu einer anderen Dokumentation wie beispielsweise GitLab Pages vereinfacht werden.

## Ausführen des Skripts

### Setup

#### Dependencies

Um die benötigten python libraries zu installieren den folgenden Befehl in einen Terminal eingeben:

```Powershell
    pip install bs4 requests dotenv
```

Alternativ kann mit der ```requirements.txt``` eine virtuelle Python Umgebung [venv](https://docs.python.org/3/library/venv.html) erstellt werden.

#### Environmental Variables

Um sich bei Atlassian authentifizieren zu können wird ein Personal Access Token (PAT) benötigt. Diesen kann man auf Confluence erstellen. Dafür:

1. Auf Confluence anmelden

![alt text](assets/image.png)

2. Das Profil aufrufen

![alt text](assets/image1.png)

3. Unter "Einstellungen" auf die Persönlichen Zugriffstoken

![alt text](assets/image-1.png)

4. Auf "Token erstellen" drücken. Jetzt dem Token einen Namen geben und ein Ablaufdatum setzten.

![alt text](assets/image-2.png)

5. Den Persönlichen Schlüssel kopieren und gut aufbewahren. Im Root Ordner des Projektes eine Datei Names ``.env`` anlegen. In dieser Datei den Token von gerade eben abspeichern. Die Datei sollte nun so aussehen:

```Powershell
    CONFLUENCE_TOKEN = "Your Token"
```

Eine Beispiel .env Datei mit dem Namen ```.env.example``` liegt im selben Ordner wie das Skript.

Das Python Skript kann nun ausgeführt werden.

##### Hinweis!

.env Dateien sind automatisch im gitignore und werden nicht mit gepusht. Sie liegen lokal auf dem eigenen Rechner und werden nicht commited. Die .env Datei wird hier verwendet um das Aufheben des Confluence Keys zu vereinfachen.

### Nutzung

Zur Nutzung des Script muss die zu Konvertierende Seite in Confluence angegeben werden. Dies wird beim ausfuehren des Scripts mit der Flag -u angehängt.

Bsp:
```
    python /path/to/convert_main.py -u https://domain.com/confluence_subpage
```

Nach dem einsetzen der gewünschten URL kann das Script ausgeführt werden. Das Ergebnis wird als Ordnerstruktur mit allen Assets außer Gliffy Diagrammen unter landing/ angelegt. Von dort aus kann der Ordner an den gewünschten Ort verschoben werden.


## Technologie

Die Markdown Dateien verwenden MDX, weshalb sie in der Lage sind HTML Elemente anzuzeigen. Ursprünglich wurde dieses Skript genutzt, um Confluence Seiten in einer durch [Docusaurus](https://docusaurus.io/) generierten Dokumentation anzuzeigen. Daher werden bestimmte JSX Elemente in der Markdown verwendet

## Probleme

Die Folgenden Problem bzw. Funktionalitäten konnten leider nicht umgesetzt werden. Dies hängt teils auch mit der späteren Implementierung in [Docusaurus](https://docusaurus.io/) zusammen.

* **Farbiger Text/Farbige Tabellen**
  * In der Confluence Seite werden für bestimmte Farben so wie spezifische Größen Style-elemente benutzt. Wenn diese einfach importiert werden schimpft docusaurus das wir jsx styling benutzen sollen. Wenn wir allerdings das styling händisch in jsx umwandeln, kriegen wir eine Fehlermeldung das ein Character namens "acorn" nicht verarbeitet werden kann. Somit ist unklar welches styling wirklich gebraucht wird und eine Formattierung nicht möglich
* **Previews von Docs**
  * In MD werden native keine Previews unterstützt, man müsste per hand ein komplexen HTML Frame um das Dokumtent und in MD implementieren. Hierbei ist das Problem, dass bevor das HTML verarbeitet wird erst in MD umgewandelt werden muss um es hier darzustellen. Dabei können weitere Fehler auftreten.
* **Embedded Links** (z.B. Jira-Issues)
  * Diese Arten von Links werden auf Confluence über Java embedded. So wird auch der derzeitige Status erhalten. Das Script fragt allerdings nur die pure HTML ab und dort sind keine Javascript generierten Elemente vorhanden. Daher ist dessen import nicht möglich.
* **Gliffy import**
  * Ähnlich zu den Jira-Tickets werden die Links zum Gliffy Editor mit javascript generiert. Man kann zwar ein Bild des Gliffys herunterladen und anzeigen, allerdings geht dadurch die Einsicht das es sich um ein Gliffy handelt und die bearbeitungsfähigkeit verloren.
* **Checkboxen/TODO**
  * Im normalen MD gibt es keine Checkboxen. In Versionen wo dies funktioniert wurde md um einige Funktionen erweitert (Beispiel git flavoured md). Um das Umzusetzten müsste man seine eigene MD Erweiterung schreiben
* **Status Flags**
  * Status Flags werden ähnlich zu Farben über css Elemente gestylt, somit ist es nicht möglich sie 1:1 zu übernehmen
* **interne Verlinkungen in der neuen Dokumentation**
  * Links auf andere Pages würden nur dann funktionieren, wenn man den gesamten Confluence Aufbau kennen würde und die Struktur sich nicht ändern würde. Somit braucht man einen website crawler welcher alle Confluence Pages durchläuft und eine Struktur erstellt, um dann die Links auf Docusaurus anzupassen. Da die Struktur der Dokumentation geändert wird, ist es nicht möglich die Links automatisiert zu verändern.
* **Formatierung**
  * Es ließen sich keine klaren Regeln für Formatierungen finden, weshalb manche Pages ein paar Umbrüche zu viel haben. Ursache davon ist die wirren Struktur von Confluence.

## Kontakt

Bei Problemen oder Fragen stehen die Folgenden Personen zur Verfügung:

- [Tim Kosleck](tim.kosleck@deutschebahn.com) -> Author
- [Jonathan Fritzsch](jonathan.fritzsch@deutschebahn.com) -> Author
- [Markus M Schmieder](markus.m.schmieder@deutschebahn.com) -> Maintainer
- [Sören Julius Carstensen](soeren-julius.carstensen@deutschebahn.com) -> Maintainer