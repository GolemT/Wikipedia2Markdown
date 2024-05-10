# Confluence2Markdown

## Erläuterung

Confluence2Markdown ist ein Python Script welches eine Confluence Seite scannt und eine Markdown Datei (.md) mit den Inhalten anfertigt. Somit soll der wechsel von Confluence zu einer anderen Dokumentation wie beispielsweise GitLab Pages vereinfacht werden.

## Technologie

Die Markdown Dateien verwenden MDX, weshalb sie in der Lage sind HTML Elemente anzuzeigen. Ursprünglich wurde dieses Skript genutzt, um Confluence Seiten in einer durch (Docusaurus)[https://docusaurus.io/] generierten Dokumentation anzuzeigen. Daher werden bestimmte JSX Elemente in der Markdown verwendet

## Probleme

Confluence ist sehr wirr gestaltet, sich eine Regeln finden lassen um Texte korrekt zu Formatieren. Daher muss leider jede Markdown Datei nochmal händisch überprüft werden. Allerdings handelt es sich dabei nur um die reine Formatierung anstatt, daher ist die Zeitersparnis dennoch immens.

## Kontakt

Bei Problemen oder Fragen stehen die Folgenden Personen zur Verfügung:

- (Tim Kosleck)[tim.kosleck@deutschebahn.com] -> Author
- (Jonathan Fritzsch)[jonathan.fritzsch@deutschebahn.com] -> Author
- (Markus M Schmieder)[markus.m.schmieder@deutschebahn.com] -> Maintainer