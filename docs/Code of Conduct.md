# Code of Conduct

## Arbeit im Team

### Halten an Absprachen

Absprachen welche im Discord oder im echten Leben (IRL) stattfinden werden eingehalten. Darunter fallen z.B.:

> Jonathan:
> Bevor irgendwas gemerged wird: fragt bitte Tim und mich nach einem Approval -- clean code policy und so

> Jonathan:
> wir nutzen alle bitte die neuste python version

> Tim:
> Ihr werdet wahrscheinlich während der Entwicklung merge konflikte bekommen. Da hilft dann ein einfacher rebase.

> Jonathan:
> -> solange das Ticket noch offen und der MR nicht erfolgreich durchgeführt / geschlossen: KEIN neues Ticket 🧐

### Issues selbstständig pullen

Wenn das vorherige Issue fertig ist (also Review, MR und das Issue auf done geschoben ist) wird sich **sofort** ein neues Issue gezogen und bearbeitet.

### Sofortige Absprache mit dem Team

Bei Themen die alle Teammitglieder betreffen, aufkommenden Problemen, Sorgen o.ä. wird sich an ander Teammitglieder oder die ganze Gruppe gewandt.

Probleme können immer auftreten oder es kann immer vorkommen, dass einem Fehler passiere - wir sind alle nur Menschen - diese können oft gelösst werden, wenn andere Personen mit eingebunden werden

Das Einzige was nicht passieren darf, ist, dass diese Sachen verschwiegen werden.

>Tim und ich beißen nicht

## Code Guidelines

### Prinzipien und Richtlinien für Clean Code

* **KISS-Prinzip (Keep It Simple, Stupid):**
  * Stelle einfache und verständliche Lösungen in den Vordergrund und vermeide unnötige Komplexität durch den Verzicht auf überflüssige Abstraktionen, Designmuster oder Algorithmen.

* **DRY-Prinzip (Don't Repeat Yourself):**
  * Fördere die Wartbarkeit und Änderungsfreundlichkeit, indem du Code-Duplikationen vermeidest und gemeinsame Funktionalitäten in wiederverwendbare Einheiten wie Funktionen, Klassen oder Module extrahierst.

* **SOLID-Prinzipien (für objektorientierte Programmierung):**
  * **Single Responsibility Principle (SRP):**
    * Erreiche eine hohe Kohäsion von Klassen und Funktionen, indem du sicherstellst, dass jede Einheit genau eine klar definierte Aufgabe erfüllt.
  * **Open/Closed Principle (OCP):**
    * Ermögliche die Erweiterung von Softwarekomponenten, ohne dass deren Quellcode direkt verändert werden muss, indem du auf Techniken wie Vererbung, Interfaces oder Komposition setzt.
  * **Liskov Substitution Principle (LSP):**
    * Stelle sicher, dass Subtypen sich korrekt verhalten und problemlos anstelle ihrer Basistypen verwendet werden können.
  * **Interface Segregation Principle (ISP):**
    * Reduziere unnötige Abhängigkeiten, indem du spezifische Interfaces definierst, die genau auf die Bedürfnisse der jeweiligen Clients zugeschnitten sind.
  * **Dependency Inversion Principle (DIP):**
    * Entkopple verschiedene Module voneinander, indem du Abhängigkeiten zu Abstraktionen (Interfaces oder abstrakte Klassen) schaffst, anstatt von konkreten Implementierungen abzuhängen.

* **YAGNI-Prinzip (You Ain't Gonna Need It):**
  * Konzentriere dich auf die Implementierung tatsächlich benötigter Funktionalitäten und vermeide es, Features zu entwickeln, die möglicherweise nie zum Einsatz kommen werden.

* **Sprechende Namen:**
  * Verbessere die Lesbarkeit und Verständlichkeit deines Codes durch die Verwendung aussagekräftiger und bedeutungsvoller Namen für Variablen, Funktionen und Klassen.

* **Flache Hierarchien:**
  * Reduziere die Komplexität, indem du tiefe Verschachtelungen vermeidest und den Code in überschaubare Einheiten mit geringer Verschachtelungstiefe strukturierst.
  
* **Vermeidung von "loose if statements":**
  * Steigere die Lesbarkeit und Wartbarkeit, indem du explizite Bedingungen verwendest und verschachtelte if-Anweisungen durch Guard Clauses oder frühe Rückgaben reduzierst.

* **Vermeidung von Seiteneffekten:**
  * Stelle sicher, dass Funktionen vorhersehbar und testbar sind, indem du Seiteneffekte vermeidest und Funktionen ausschließlich ihren definierten Zweck erfüllen lässt.

* **Verwendung von Konstanten:**
  * Erhöhe die Lesbarkeit und Wartbarkeit, indem du magische Zahlen durch benannte Konstanten ersetzt.

* **Qualitativ hochwertige Kommentare:**
  * Dokumentiere nicht-offensichtliche Aspekte des Codes, indem du das "Warum" hinter Entscheidungen erläuterst und Kommentare prägnant hältst.

* **Einheitliche Formatierung:**
  * Sorge für eine gute Lesbarkeit und Konsistenz des Codes, indem du automatische Formatierer verwendest und Coding-Konventionen einhältst.

### Nutzung von KI

Die Nutzung von AI ist gestattet. Allerdings nur wenn der Code auch wirklich verstanden wird bzw. wenn nicht einfach nur Copy+Paste genutzt wird. Sollte das der Fall sein **muss** der folgende Block für den Reviewer hinzugefügt werden:

```python
// Folgende Passage ist mit AI generiert worden //
/////////////////////////////////////////////////
fun main ():
    print("Hello World!")

//////////////////////////////////////////////
```

Diese Passage darf nach dem Review Prozess entfernt werden. Es muss dem Reviewer klar sein das diese Passage nicht durch einen Menschen geschrieben wurde und noch überprüft/umgeschrieben werden muss.

### Issue Vorgaben

Issue namen beschreiben was in dem Issue getan werden soll bzw was das Ziel ist. Hier wird **nicht** das Problem beschrieben. Zudem **muss** so viel Kontext wie möglich gegeben werden. Dazu gehört:

* Auf welcher Website taucht der Fehler auf
* An welcher Stelle der Website passiert der Fehler (Bitte das genau Element finden)
* Was ist der genaue Fehler
* Ausschnitt aus dem Log File/Console output

Beispiel eines schlechten Issues:

> Tabellenfehler
>
> Wenn man ne Tabelle verarbeitet kommt ein Fehler

Beispiel eines guten Issues:

> Improve Table Handling
>
> Wenn man die CLI zur Konvertierung der Website "https://wikipedia/beispiel" nutzt, erhählt man folgenden Fehler ```ValueError: Not a Value```. Dieser entsteht bei folgender Passage: ![Bild von der Website/ Ursache]. Hier ist ein Auszug des Logs: ```Error Log```. Dieser Fehler muss behoben werden um weiterhin Webseiten verarbeiten zu können

### Branch Names

Branches werden durch Issues erzeugt. Daher wird der Name immer durch das dazugehörige Issue erstellt. Vor den Issuenamen kommt dann entweder ein ```feature/``` oder ein ```bug/```. Durch die automatische Generierung von Branches durch Issues wird das Feature flag direkt davor geschrieben. Daher ist nur bei bugs eine manuelle Branch Namensnänderung nötig.

### Kein Branch ohne Issue

Es werden keine Branches erstellt ohne das ein zugehöriges Issue erstellt wurde. Solche branches werden gnadenlos **gelöscht**.

### Kein Issue ohne Absprache

Issues können in Gitlab angelegt werden und gelten dann als ```experimental idea```. Es braucht das nachlesen eines anderen um das Issue als vollwertig in den Backlog zu schieben. Das Issue wird nicht angefangen, bevor es im Backlog liegt.

### Kein Change ohne Merge Request

Jeder Change im Gitlab muss durch eine Merge Request in Main gemerged werden. Direkte pushes/commits zu main sind unzulässig.
