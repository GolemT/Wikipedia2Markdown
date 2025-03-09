# Screen Scraping



aus Wikipedia, der freien Enzyklopädie





Der Begriff 
Screen Scraping

 (engl., etwa: „am Bildschirm schürfen“) umfasst generell alle Verfahren zum Auslesen von Texten aus Computerbildschirmen. Gegenwärtig wird der Ausdruck jedoch beinahe ausschließlich in Bezug auf 
[Webseiten](https://de.wikipedia.org/wiki/Webseite)
 verwendet (daher auch 
Web Scraping

 oder 
Web Harvesting

). In diesem Fall bezeichnet Screen Scraping speziell die 
[Techniken](https://de.wikipedia.org/wiki/Technik)
, die der Gewinnung von 
[Informationen](https://de.wikipedia.org/wiki/Information)
 durch gezieltes Extrahieren der benötigten 
[Daten](https://de.wikipedia.org/wiki/Daten)
 dienen.





## Einsatzgebiete





#### Suchmaschinen und Web Mining





Suchmaschinen verwenden sogenannte 
[Crawler](https://de.wikipedia.org/wiki/Webcrawler)
 zum Durchsuchen des 
[World Wide Web](https://de.wikipedia.org/wiki/World_Wide_Web)
, zur Analyse von Webseiten und Sammeln von Daten, wie 
[Web-Feeds](https://de.wikipedia.org/wiki/Web-Feed)
 oder 
[E-Mail-Adressen](https://de.wikipedia.org/wiki/E-Mail-Adresse)
. Screen-Scraping-Verfahren werden auch beim 
[Web Mining](https://de.wikipedia.org/wiki/Web_Mining)
 angewandt.




#### Ersatz von Web Services





Um den Abruf und die Weiterverarbeitung von Informationen aus Webseiten für den 
[Kunden](https://de.wikipedia.org/wiki/Kunde)
 deutlich zu erleichtern, hat der Anbieter des Seiteninhalts (auch Content-Anbieter) die Möglichkeit, die Daten nicht nur in Form einer (menschenlesbaren) Webseite darzustellen, sondern sie zusätzlich in einem maschinenlesbaren 
[Format](https://de.wikipedia.org/wiki/Dateiformat)
 (etwa 
[XML](https://de.wikipedia.org/wiki/Extensible_Markup_Language)
) aufzubereiten. Gezielt abgefragte Daten könnten dem Kunden dadurch als 
[Webservice](https://de.wikipedia.org/wiki/Webservice)
 zur 
[automatisierten](https://de.wikipedia.org/wiki/Automat)
 Weiterverarbeitung zur Verfügung gestellt werden.


Häufig hat der Content-Anbieter jedoch kein Interesse an dem mechanisierten Abruf seiner Daten bzw. der automatisierten Nutzung seines Dienstes (insbesondere bezüglich spezieller Funktionen, die ausschließlich realen Nutzern vorbehalten sein sollten), oder die Errichtung eines Web Service wäre mit zu hohen 
[Kosten](https://de.wikipedia.org/wiki/Kosten)
 verbunden und daher unwirtschaftlich. In solchen Fällen kommt häufig das Screen Scraping zum Einsatz, um die gewünschten Daten dennoch aus der Webseite zu filtern.




#### Erweitertes Browsen





Screen Scraping kann zum Einsatz kommen, um den Browser mit weiteren Funktionen auszustatten oder bisher umständliche Vorgänge zu vereinfachen. So können Anmeldevorgänge bei Foren automatisiert oder Dienste einer Webseite abgerufen werden, ohne dass der Nutzer die Webseite besuchen muss, sondern etwa über eine Browser-Symbolleiste.


Eine einfache Form von derartigen Screen Scrapern stellen 
[Bookmarklets](https://de.wikipedia.org/wiki/Bookmarklet)
 dar.




#### Remixing





Remixing ist eine Technik, bei der Webinhalte verschiedener Dienste zu einem neuen Dienst verbunden werden (
siehe auch

 
[Mashup](https://de.wikipedia.org/wiki/Mashup_(Internet))
). Wenn keine offenen Programmierschnittstellen zur Verfügung stehen, muss hier ebenfalls auf Screen-Scraping-Mechanismen zurückgegriffen werden.




#### Missbrauch





Screen-Scraping-Techniken können jedoch auch missbraucht werden, indem Inhalte fremder Webseiten gegen den Willen des Anbieters kopiert und auf einem eigenen Server angeboten werden. Gerade durch das Training ‚
[künstlicher Intelligenz](https://de.wikipedia.org/wiki/K%C3%BCnstliche_Intelligenz)
‘ (KI) wie 
[Chatbots](https://de.wikipedia.org/wiki/Large_Language_Model)
 und 
[Bildgeneratoren](https://de.wikipedia.org/wiki/Text-zu-Bild-Generator)
 kommt es zu einem zunehmenden Wettkampf von Webscraping durch kommerzielle KI-Unternehmen und Abwehrmaßnahmen von Online-Portalen und -Medien.
[[1]](#cite_note-1)






## Funktionsweise





Screen Scraping besteht im Wesentlichen aus zwei Schritten:




* Abrufen von Webseiten
* Extraktion der relevanten Daten



### Abrufen von Webseiten





##### Statische Webseiten





Idealerweise befinden sich die interessanten Daten auf einer Webseite, die über eine 
[URL](https://de.wikipedia.org/wiki/Uniform_Resource_Locator)
 abgerufen werden kann. Alle für den Abruf der Informationen benötigten Parameter werden über URL-Parameter (
[Query-String](https://de.wikipedia.org/wiki/Query-String)
, siehe 
[GET-Request](https://de.wikipedia.org/wiki/HTTP#HTTP_GET)
) übergeben. In diesem einfachen Fall wird einfach die Webseite heruntergeladen und die Daten werden mit einem geeigneten Mechanismus extrahiert.




##### Formulare





In vielen Fällen werden die Parameter durch Ausfüllen eines 
[Webformulars](https://de.wikipedia.org/wiki/Webformular)
 abgefragt. Dabei werden die Parameter oft nicht in der URL übergeben, sondern im Nachrichtenkörper (
[POST-Request](https://de.wikipedia.org/wiki/HTTP#HTTP_POST)
).




##### Personalisierte Webseiten

Viele Webseiten enthalten personalisierte Informationen. Das 
[Hypertext Transfer Protocol](https://de.wikipedia.org/wiki/Hypertext_Transfer_Protocol)
 (HTTP) bietet jedoch keine native Möglichkeit, Anfragen einer bestimmten Person zuzuordnen. Um eine bestimmte Person wiederzuerkennen, muss die Serveranwendung auf HTTP aufgesetzte 
[Sitzungskonzepte](https://de.wikipedia.org/wiki/Sitzung_(Informatik))
 verwenden. Eine häufig genutzte Möglichkeit ist die Übertragung von 
[Session-IDs](https://de.wikipedia.org/wiki/Session-ID)
 durch die URL oder durch 
[Cookies](https://de.wikipedia.org/wiki/HTTP-Cookie)
. Diese Sitzungskonzepte müssen von einer Screen-Scraping-Anwendung unterstützt werden.


### Datenextraktion

Ein Programm zur Extraktion von Daten aus Webseiten wird auch 
[Wrapper](https://de.wikipedia.org/wiki/Wrapper_(Informationsextraktion))
 genannt.


Nachdem die Webseite heruntergeladen wurde, ist es für die Extraktion der Daten zunächst wichtig, ob der genaue Ort der Daten auf der Webseite bekannt ist (etwa 
zweite Tabelle, dritte Spalte).


Wenn dies der Fall ist, stehen für die Extraktion der Daten verschiedene Möglichkeiten zur Verfügung. Man kann zum einen die heruntergeladenen Webseiten als Zeichenketten interpretieren und etwa mit 
[regulären Ausdrücken](https://de.wikipedia.org/wiki/Regul%C3%A4rer_Ausdruck)
 die gewünschten Daten extrahieren.


Wenn die Webseite 
[XHTML](https://de.wikipedia.org/wiki/Extensible_Hypertext_Markup_Language)
-konform ist, bietet sich die Nutzung eines XML-
[Parsers](https://de.wikipedia.org/wiki/Parser)
 an. Für den Zugriff auf XML gibt es zahlreiche unterstützende Techniken (
[SAX](https://de.wikipedia.org/wiki/Simple_API_for_XML)
, 
[DOM](https://de.wikipedia.org/wiki/Document_Object_Model)
, 
[XPath](https://de.wikipedia.org/wiki/XPath)
, 
[XQuery](https://de.wikipedia.org/wiki/XQuery)). Oft werden die Webseiten jedoch lediglich im (möglicherweise sogar fehlerhaften) 
[HTML](https://de.wikipedia.org/wiki/Hypertext_Markup_Language)
-Format ausgeliefert, welches nicht dem XML-Standard entspricht. Mit einem geeigneten Parser lässt sich unter Umständen dennoch ein XML-konformes Dokument herstellen. Alternativ kann das HTML vor dem Parsen mit 
[HTML Tidy](https://de.wikipedia.org/wiki/HTML_Tidy)
 bereinigt werden. Manche Screen Scraper verwenden eine eigens für HTML entwickelte Anfragesprache.


Ein Kriterium für die Güte der Extraktionsmechanismen ist die Robustheit gegenüber Änderungen an der Struktur der Webseite. Hierfür sind fehlertolerante Extraktionsalgorithmen erforderlich.


In vielen Fällen ist die Struktur der Webseite jedoch unbekannt (etwa beim Einsatz von Crawlern). Datenstrukturen wie etwa Kaufpreisangaben oder Zeitangaben müssen dann auch ohne feste Vorgaben erkannt und interpretiert werden.




## Architektur





### Zentralisierte Architektur





Ein Screen Scraper kann auf einem speziellen 
[Webserver](https://de.wikipedia.org/wiki/Webserver)
 installiert sein, der in regelmäßigen Abständen oder auf Anfrage die geforderten Daten abruft und seinerseits in aufbereiteter Form anbietet. Dieses serverseitige Vorgehen kann jedoch unter Umständen rechtliche Probleme mit sich ziehen und vom Content-Anbieter auch leicht durch Blockieren der Server-
[IP](https://de.wikipedia.org/wiki/IP-Adresse)
 verhindert werden.




### Verteilte Architektur





Beim verteilten Vorgehen werden die Informationen direkt vom Client abgerufen. Je nach Anwendung werden die Informationen in einer Datenbank gespeichert, an andere Anwendungen weitergegeben oder aufbereitet im Browser angezeigt. Die verteilte Architektur kann nicht nur schwieriger blockiert werden, sondern skaliert auch besser.

## Anbieterseitige Abwehrmaßnahmen
Viele Content-Anbieter haben kein Interesse an einem isolierten Abrufen bestimmter Informationen. Grund dafür kann sein, dass sich der Anbieter durch Werbeeinblendungen finanziert, die durch Screen Scraping leicht gefiltert werden können. Zudem könnte der Content-Anbieter ein Interesse daran haben, den Benutzer zu einer bestimmten Navigationsreihenfolge zu zwingen. Um diese Interessen zu gewährleisten, gibt es verschiedene Strategien.




### Kontrolle des Benutzerverhaltens





Der Server zwingt den Benutzer durch Verwenden von Session-IDs zu einer bestimmten Navigationsreihenfolge. Beim Aufruf der Verkehrslenkungsseite des Webangebotes wird eine temporär gültige Session-ID erzeugt. Diese wird über die URL, versteckte Formularfelder oder durch Cookies übertragen. Wenn ein Nutzer oder ein Bot durch einen 
[Deep Link](https://de.wikipedia.org/wiki/Deep_Link)
 auf die Seite stößt, kann er keine gültige Session-ID vorweisen. Der Server leitet ihn dann auf die Verkehrslenkungsseite um. Diese Strategie verwendet beispielsweise 
[eBay](https://de.wikipedia.org/wiki/EBay)
, um Deep Links auf Auktionslisten zu verhindern. Ein speziell programmierter Screen Scraper kann sich jedoch zunächst eine gültige Session-ID holen und dann die gewünschten Daten herunterladen.


Das folgende Beispiel zeigt einen 
[JavaScript](https://de.wikipedia.org/wiki/JavaScript)
-basierten Screen Scraper, der die von eBay benutzte Strategie umging. Es lud sich zunächst die Hauptseite herunter, extrahierte mit einem regulären Ausdruck eine gültige URL (in diesem Fall die Liste der Auktionen, bei denen Disketten ersteigert werden) und öffnete diese im Browser.

```javascript
function EbayScraper() {
    req = new XMLHttpRequest();
    req.open('GET', 'http://computer.ebay.de', false);
    req.send(null);
    var regex = new RegExp('http:\/\/computer\.listings\.ebay\.de\/Floppy-Zip-Streamer_Disketten_[a-zA-Z0-9]*');
    window.location = req.responseText.match(regex);
 }
```






Neben der Zweckentfremdung von Session-IDs gibt es weitere Möglichkeiten, das Benutzerverhalten zu überprüfen:




* Kontrolle des[Referrers](https://de.wikipedia.org/wiki/Referrer)zur Abwehr von Deep Links
* Kontrolle, ob in die Seite eingebettete Elemente (Grafiken etc.) zeitnah heruntergeladen werden
* Kontrolle, ob JavaScript-Elemente ausgeführt werden



Alle diese Methoden beinhalten jedoch gewisse Problematiken, etwa weil Referrer-Angaben nicht zwingend sind, weil eingebettete Elemente möglicherweise von einem 
[Proxy](https://de.wikipedia.org/wiki/Proxy_(Rechnernetz))
 oder aus dem 
[Cache](https://de.wikipedia.org/wiki/Cache)
 geliefert werden oder weil der Anwender schlichtweg die Anzeige von Grafiken oder das Ausführen von JavaScript deaktiviert hat.




### Unterscheiden zwischen Mensch und Bot





Der Server versucht vor dem Ausliefern der Daten zu erkennen, ob es sich beim 
[Client](https://de.wikipedia.org/wiki/Client)
 um einen von einem Menschen benutzen Browser oder um einen 
[Bot](https://de.wikipedia.org/wiki/Bot)
 handelt. Eine häufig eingesetzte Methode dafür ist die Verwendung von 
[Captchas](https://de.wikipedia.org/wiki/Captcha)
. Dabei wird dem Client eine Aufgabe gestellt, welche für Menschen möglichst einfach, für eine Maschine jedoch sehr schwer lösbar ist. Dies kann eine Rechenaufgabe oder das Abtippen von Buchstaben sein, wobei oft die Schwierigkeit für die Maschine im Erkennen der Aufgabe liegt. Dies kann z. B. erreicht werden, indem die Rechenaufgabe nicht als Text, sondern als Bild übermittelt wird.


Captchas werden für bestimmte Online-Dienste wie Foren, Wikis, Downloadseiten oder Online-Netzwerke eingesetzt etwa gegen automatisches Registrieren, automatisches Ausspähen von Profilen anderer Nutzer sowie automatische Downloads durch Bots. Mitunter muss ein Client erst nach einer bestimmten Anzahl von Aktionen ein Captcha lösen.


Theoretisch lassen sich für alle Captchas auch Bots entwickeln, die diese Aufgaben auf Basis von 
[Optical Character Recognition](https://de.wikipedia.org/wiki/Optical_Character_Recognition)
 (Extraktion der Aufgabe aus einem Bild) lösen können, so dass dieser Schutz umgangen werden kann. Des Weiteren besteht die Möglichkeit, die Teilaufgabe an einen Menschen weiterzugeben, so dass dieser das Captcha für die Maschine löst. Beides bedeutet jedoch einen erheblichen Mehraufwand für den Botbetreiber.




### Verschleierung





Die Informationen werden in für Maschinen nicht oder nur schwer lesbarer Form angeboten. Etwa als Grafik, in 
[Flash-Animationen](https://de.wikipedia.org/wiki/Adobe_Flash)
 oder 
[Java-Applets](https://de.wikipedia.org/wiki/Java-Applet)
. Allerdings leidet hierunter häufig die 
[Gebrauchstauglichkeit](https://de.wikipedia.org/wiki/Gebrauchstauglichkeit_(Produkt))
.


Zur Verschleierung der Daten kann auch 
[JavaScript](https://de.wikipedia.org/wiki/JavaScript)
 zum Einsatz kommen. Diese Methode wird vor allem auch gegen 
[E-Mail-Harvester](https://de.wikipedia.org/wiki/E-Mail-Harvester)
 eingesetzt, die E-Mail-Adressen zur Versendung von 
[Spam](https://de.wikipedia.org/wiki/Spam)
 sammeln. Die eigentlichen Daten werden nicht im HTML-Code übertragen, sondern werden erst durch JavaScript in die Webseite geschrieben. Die Daten können zusätzlich verschlüsselt übertragen und erst beim Anzeigen der Seite entschlüsselt werden. Mit Hilfe eines 
[Obfuscators](https://de.wikipedia.org/wiki/Obfuskation_(Software))
 kann der Programmcode verschleiert werden, um die Entwicklung eines Screen Scrapers zu erschweren.


Einfaches Beispiel zur Verschleierung einer E-Mail-Adresse mit JavaScript (ohne Verschlüsselung):


```javascript
 function mail() {
     var name = "info";
     var domain = "example.com";
     var mailto = 'mailto:' + name + '@' + domain;
     document.write(mailto);
  }

```

## Erstellung von Screen Scrapern





Je nach Komplexität der Aufgabe muss ein Screen Scraper neu programmiert werden. Mithilfe von Toolkits lassen sich Screen Scraper jedoch auch ohne Programmierkenntnisse erstellen. Für die Implementierungsform gibt es verschiedene Möglichkeiten, etwa als 
[Bibliothek](https://de.wikipedia.org/wiki/Programmbibliothek)
, als 
[Proxy-Server](https://de.wikipedia.org/wiki/Proxy-Server)
 oder als eigenständiges Programm.




## Anwendungen

Piggy Bank
 war eine vom Simile-Projekt am 
[MIT](https://de.wikipedia.org/wiki/Massachusetts_Institute_of_Technology)
 entwickelte Erweiterung für 
[Firefox](https://de.wikipedia.org/wiki/Mozilla_Firefox)
. Mit ihr ließen sich Verknüpfungen von Diensten verschiedener Anbieter realisieren. Es erkannte automatisch auf einer Webseite angebotene 
[RDF](https://de.wikipedia.org/wiki/Resource_Description_Framework)
-Ressourcen. Diese konnten gespeichert, verwaltet und mit anderen Diensten (etwa geographische Informationen mit 
[Google Maps](https://de.wikipedia.org/wiki/Google_Maps)
) kombiniert werden. Piggy Bank wird nicht mehr angeboten. Als Ersatz bietet sich Selenium
[[2]](#cite_note-2)
 an, womit man einen Web-Browser wie Firefox programmatisch steuern kann.


Eine weitere bekannte Firefox-Erweiterung ist 
[Greasemonkey](https://de.wikipedia.org/wiki/Greasemonkey). Sie erlaubt es dem Nutzer eigene JavaScript-Dateien im Browser auszuführen, die das Erscheinungsbild und Verhalten der angezeigten Webseite individualisieren können, ohne einen Zugriff auf die eigentliche Webseite zu benötigen. Dadurch ist es beispielsweise möglich, Webseiten um Funktionen zu erweitern, Fehler in der Darstellung zu beheben, Inhalte von anderen Webseiten einzubinden und wiederkehrende Aufgaben automatisch zu erledigen.
[A9](https://de.wikipedia.org/wiki/A9.com)
 von 
[Amazon](https://de.wikipedia.org/wiki/Amazon.com)
 ist ein Beispiel für eine zentralisierte Remix-Architektur. A9 kann Suchergebnisse aus verschiedenen Webdiensten wie 
[Windows Live](https://de.wikipedia.org/wiki/Windows_Live)
, 
[Wikipedia](https://de.wikipedia.org/wiki/Wikipedia)
, answers.com und vielen anderen in einem Fenster anzeigen.




## Programmierbibliotheken

Programmierkundige nutzen oft 
[Skriptsprachen](https://de.wikipedia.org/wiki/Skriptsprache)
 für maßgeschneiderte Screenscraping-Projekte. Für 
[Python](https://de.wikipedia.org/wiki/Python_(Programmiersprache))
 etwa gibt es die Programmbibliothek 
[Beautiful Soup](https://de.wikipedia.org/wiki/Beautiful_Soup)
, [[3]](#cite_note-3)
 die den Umgang mit real existierendem 
[HTML](https://de.wikipedia.org/wiki/Hypertext_Markup_Language) erleichtert. Ebenfalls auf Python basiert die [domänenspezifische Sprache](https://de.wikipedia.org/wiki/Dom%C3%A4nenspezifische_Sprache) [redex](/w/index.php?title=Redex&action=edit&redlink=1) (Regular Document Expressions)
[[4]](#cite_note-4)

 von Marcin Wojnarski, die speziell für das Webscraping geschaffen wurde und die Lücke zwischen den praktischen, aber kleinteiligen regulären Ausdrücken und der mächtigen, aber sehr rigiden 
[XPath](https://de.wikipedia.org/wiki/XPath)
-Syntax schließen soll.
[[5]](#cite_note-5)

## Rechtliche Probleme

Beim Scraping von Webseiten fremder Anbieter muss auf die Einhaltung der 
[Urheberrechte](https://de.wikipedia.org/wiki/Urheberrecht)
 geachtet werden, vor allem wenn die Inhalte über ein eigenes Angebot eingebunden werden. Eine rechtliche Grauzone ist dagegen das Anbieten von Programmen, die ein clientseitiges Screen Scraping ermöglichen. Einige Anbieter verbieten das automatische Auslesen von Daten auch explizit in den Nutzungsbedingungen.
[[6]](#cite_note-6)

Ein weiteres Problem stellt unter Umständen das Ausblenden von Informationen dar, etwa von Werbung oder rechtlich relevanten Informationen wie 
[Disclaimer](https://de.wikipedia.org/wiki/Disclaimer)
, Warnungen oder gar die automatische Bestätigung der 
[AGB](https://de.wikipedia.org/wiki/Allgemeine_Gesch%C3%A4ftsbedingungen)
 durch den Screen Scraper, ohne dass der Nutzer diese zu Gesicht bekommt.


## Siehe auch

* [Webintegration](https://de.wikipedia.org/wiki/Webintegration)

## Literatur

* Max Völkel:[Extraktion von XML aus HTML-Seiten.](http://www.xam.de/2003/05/diplomathesis/Extraktion%20von%20XML%20aus%20HTML-Seiten%20-%20Das%20WYSIWYG-Werkzeug%20d2c%20-%20Ausarbeitung.pdf)(PDF; 2,6 MB) 2003.
* Markus Weißmann:[Vergleich von Wrappersystemen.](http://www.mweissmann.de/downloads/Vergleich_von_Wrappersystemen.pdf)(PDF; 276 kB) 2002.
* Gerald Huck, Peter Fankhauser, Karl Aberer, Erich Neuhold:[Jedi: Extracting and Synthesizing Information from the Web.](http://infoscience.epfl.ch/record/54322/files/P1998-11.pdf)(PDF; 140 kB) 1998 (englisch)
* Ling Liu, Carlton Pu, and Wei Han:[XWRAP: An XMLenabled Wrapper Construction System for Web Information Sources.](http://citeseer.ist.psu.edu/215418.html)2000. (englisch)

## Weblinks

* [Data extraction for Web 2.0: Screen scraping in Ruby/Rails](https://web.archive.org/web/20100815013348/http://www.rubyrailways.com/data-extraction-for-web-20-screen-scraping-in-rubyrails/)([Memento](https://de.wikipedia.org/wiki/Web-Archivierung#Begrifflichkeiten)vom 15. August 2010 im[Internet Archive](https://de.wikipedia.org/wiki/Internet_Archive)) (englisch)
* [Screen-scraping with WWW::Mechanize](http://www.perl.com/pub/a/2003/01/22/mechanize.html)(englisch)

## Einzelnachweise

1. [↑](#cite_ref-1)Jason Koebler:[Websites are Blocking the Wrong AI Scrapers (Because AI Companies Keep Making New Ones).](https://www.404media.co/websites-are-blocking-the-wrong-ai-scrapers-because-ai-companies-keep-making-new-ones/)In:404 Media.29. Juli 2024,abgerufen am 30. Juli 2024(englisch).
2. [↑](#cite_ref-2)[Selenium-Website](http://seleniumhq.org/)
3. [↑](#cite_ref-3)[Homepage der Python-BibliothekBeautiful Soup](http://www.crummy.com/software/BeautifulSoup/)
4. [↑](#cite_ref-4)[Referenzimplementierung von redex in der Python-Bibliotheknifty](https://github.com/mwojnars/nifty)
5. [↑](#cite_ref-5)[Erwähnung vonredexauf der Global Open Access List am 9. Oktober 2014](http://mailman.ecs.soton.ac.uk/pipermail/goal/2014-October/002971.html)
6. [↑](#cite_ref-6)[StudiVZ AGB](http://www.studivz.net/l/terms)Ziffer 5.4.3



Abgerufen von „
[https://de.wikipedia.org/w/index.php?title=Screen_Scraping&oldid=252580736](https://de.wikipedia.org/w/index.php?title=Screen_Scraping&oldid=252580736)
“




[Kategorie](https://de.wikipedia.org/wiki/Wikipedia:Kategorien)
: 
* [Angewandte Informatik](https://de.wikipedia.org/wiki/Kategorie:Angewandte_Informatik)






