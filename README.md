# GraphWithPython
Eine Möglichkeit, Graphenalgorithmen mit Python im Schulunterricht zu behandeln.

Auf der Basis der Python-Biobliothek
- `networkx`

wurde eine Bibliothek 
- `nrw_graph`
entworfen, die es erlaubt, gewisse Graphenalgorithmen methodisch/didaktisch zu vermitteln.

Um die Jupyter-Notebooks nutzen zu können, muss man die o.g. Bibliothek (networkx) installieren. Siehe dazu auch

`https://networkx.org/documentation/stable/index.html`

## Weitere Anmerkungen:
1. Bisher sind die Graphen ungerichtet.
1. Die Kanten und Knoten können mit beliebigen Attributen versehen werden.
1. Die o.g. Bibliothek (nrw_graph) stellt diverse Funktionen zur Verfügung. Viele der Funktionen nutzen die Python-Möglichkeit der Zusicherung von Vorbedingungen mittels *assert*. 
    1. Das hat zur Folge, dass die Algorithmen sehr langsam laufen. Wenn man auf diese Zusicherungen verzichtet, kann es zwar zu Laufzeitfehlern mit z.T. nicht hilfreichen fehlermeldungen kommen, doch die Laufzeit ist erheblich besser.
    1. Die Bibliothek `nrw_graph_unsafe` hat keine assert-Anweisungen. Man kann dann in den Import-Anweisungen diese Bibliothek statt der sicheren Variante nutzen.
    
 1. Einige CSV-Dateien sind beigefügt, in denen Graphen zum Testen enthalten sind:
    - **AutobahnAbschnitte.txt** (mit Langnamen aller Autobahnabfahrten)
    - **Highway.txt** (wie oben, jedoch mit geänderter Spaltenreihenfolge)
    - **staedte.txt** (ein minimaler Autobahngraph mit Langnamen einiger Städte)
    - **stdt.txt** (wie oben, jedoch mit Autokennzeichen der Städte zur Vereinfachung)





