import networkx as nx
import pandas as pd

class nrw_graph (nx.Graph):
    
    def __init__(self):
        '''
            Es wird ein leerer ungerichteter Graph erzeugt.
            
            Knoten und Kanten können mit beliebigen Attributen versehen werden.
           
        '''
        super().__init__()
            
#########################################
    
## Graph aus csv-Datei einlesen:

    def graphEinlesen(self, 
                      dateiname, 
                      sep = ",",
                      header = 0,
                     ):
        df = pd.read_csv(dateiname, header = 0, names = ["Start", "Ziel", "Entfernung"])
        
        for i in df.index:
            s = df["Start"][i] 
            z = df["Ziel"][i] 
            e = df["Entfernung"][i]
            self.fuegeKnotenHinzu (s)
            self.fuegeKnotenHinzu (z)
            self.fuegeKanteHinzu (s,z)
            self.gewichteKante (s,z,e)


## Zunächst einige Funktionen für Knoten:
    
    def fuegeKnotenHinzu(self, knoten, **args):
        '''
            ein neuer Knoten (ggf. mit weiteren Attributen) wird dem Graphen hinzugefügt.
        '''
        if not 'besucht' in args:
            args['besucht'] = False
        self.add_node(knoten, **args)
        
    def alleKnoten(self):
        '''
            liefert eine Liste aller Knoten.
        '''
        return list(self.nodes())
    
    def getKnotenAttribut(self, node, attrName):
        '''
            liefert den durch 'attrName' spezifizierten 
            Attribut-Wert des Knotens.
        '''
 #       assert self.knotenExists (node) , f"Knoten {node} gibt es nicht!"
 #       assert self.knotenHatAttribut(node, attrName), f"Knoten {node} hat kein Attribut {attrName}"
        
        return self.nodes[node][attrName]
    
    def getKnotenAttribute(self, node):
        '''
            liefert ein Dictionary der Attribute des Knotens.
        '''
 #       assert self.knotenExists (node) , f"Knoten {node} gibt es nicht!"
        
        return self.nodes[node]
        
    def setKnotenAttribut(self, node, attrName, attrWert):
        '''
            Der angegebene Knoten erhält
            unter dem angegebenen AttributNamen
            den angegebenen Wert.
            
            Ggf. wird ein neues Attribut mit dem
            angegebenen Wert erzeugt.
        '''
#        assert self.knotenExists (node) , f"Knoten {node} gibt es nicht!"

        self.nodes[node][attrName] = attrWert
        
# Hilfsfunktionen, nur relevant für die assert-Aufrufe
        
    def getKnotenMitAttribut(self, attr):
        return nx.get_node_attributes(self,attr)
    
    def knotenHatAttribut(self, node, attr):
        dic = self.getKnotenMitAttribut(attr)
        return node in dic
    
    def knotenExists(self, node):
        alle = self.alleKnoten()
        return node in alle
        
# Beispielhaft können hier Knoten 
# mit dem Attribut 'marke' versehen werden
# und als besucht markiert werden.
# einer (boolschen) Flagge versehen.

    def markiereKnoten(self, node, marke):
        '''
            Der angegebene Knoten erhält die angegebene Marke.
        '''
        self.setKnotenAttribut(node, 'marke', marke)
        
    def getKnotenMarke(self, node):
        '''
            Die Markierung des angegebenen Knoten wird geliefert.
        '''
        return self.getKnotenAttribut(node, 'marke')

    def besucheKnoten(self, node):
        '''
            der angegebene Knoten wird als besucht markiert.
        '''
        self.setKnotenAttribut(node, 'besucht', True)
        
        
    def verlasseKnoten(self, node):
        '''
            der angegebene Knoten wird als unbesucht markiert.
        '''
        self.setKnotenAttribut(node, 'besucht', False)
        
    def knotenIstBesucht(self, node):
        '''
            Es wird True geliefert genau dann,
            wenn der angegebene Knoten 
            als besucht markiert wurde.
        '''
        return self.getKnotenAttribut(node, 'besucht')

# Und einige Funktionen für Kanten: 

    def fuegeKanteHinzu(self, start, ziel, **args):
        '''
            eine neue Kante (ggf. mit weiteren Attributen) 
            zwischen den angegebenen Knoten wird dem Graphen hinzugefügt.
            
            Die Endknoten werden ggf. neu erzeugt.
        '''
        self.fuegeKnotenHinzu(start)
        self.fuegeKnotenHinzu(ziel)
        
        self.add_edge(start, ziel, **args)
        
    def alleKanten(self):
        '''
            liefert eine Liste aller Kanten.
        '''
        return list(self.edges())

    def getKantenAttribute(self, start, ziel):
        '''
            liefert ein Dictionary der Attribute der Kante.
        '''
 #       assert self.knotenExists (start) , f"Knoten {start} gibt es nicht!"
 #       assert self.knotenExists (ziel) , f"Knoten {ziel} gibt es nicht!"
 #       assert self.kanteExists (start, ziel), f"Kante {start} - {ziel} gibt es nicht!"

        return self.edges[start, ziel]
        
    def getKantenAttribut(self, start, ziel, attr):
        '''
            liefert den durch 'attr' spezifizierten Attribut-Wert der Kante
        '''

#        assert self.knotenExists (start) , f"Knoten {start} gibt es nicht!"
#        assert self.knotenExists (ziel) , f"Knoten {ziel} gibt es nicht!"
#        assert self.kanteExists (start, ziel), f"Kante {start} - {ziel} gibt es nicht!"
#        assert self.kanteHatAttribut (start, ziel, attr), f"Kante {start} - {ziel} hat kein Attribut {attr}!"

        return self.edges[start, ziel][attr]
        
    def setKantenAttribut(self, start, ziel, attrName, attrWert):
        
#        assert self.knotenExists (start) , f"Knoten {start} gibt es nicht!"
#        assert self.knotenExists (ziel) , f"Knoten {ziel} gibt es nicht!"
#        assert self.kanteExists (start, ziel), f"Kante {start} - {ziel} gibt es nicht!"

        self.edges[start, ziel][attrName] = attrWert
        
    # Die folgenden Funktionen erlauben es, 
    # der Kante eine Farbe und ein Gewicht zu geben.

    def faerbeKante(self, start, ziel, farbe):
        '''
            Die angegebene Kante wird mit der angegebenen Farbe gefärbt.
        '''

        self.setKantenAttribut(start, ziel,'farbe',farbe)
                
    def gewichteKante(self, start, ziel, gewicht):
        '''
            Die angegebene Kante wird mit dem angegebenen Gewicht versehen.
        '''

        self.setKantenAttribut(start, ziel,'gewicht',gewicht)

    # Die eingetragenen Werte können ausgelesen werden:   
    
    def getKantenFarbe(self, start, ziel):
        '''
            liefert die Farbe der Kante, sofern vorhanden; ansonsten "?"
        '''

        return self.getKantenAttribut(start, ziel, 'farbe')

    def getKantenGewicht(self, start, ziel):
        '''
            liefert das Gewicht der Kante, sofern vorhanden; ansonsten "?"
        '''

        return self.getKantenAttribut(start, ziel, 'gewicht')
    
    def alleNachbarknoten(self, start):
#       assert self.knotenExists (start) , f"Knoten {start} gibt es nicht!"
        return [ziel for ziel in self.alleKnoten() if self.kanteExists(start, ziel)]

    
# Hilfsfunktionen, nur relevant für die assert-Aufrufe
    
    def getKantenMitAttribut(self, attr):
        return nx.get_edge_attributes(self,attr)
    
    def kanteHatAttribut(self, start, ziel, attr):
        dic = self.getKantenMitAttribut(attr)
        return (start, ziel) in dic or (ziel, start) in dic
    
    def kanteExists(self, start, ziel):
        kanten = self.alleKanten()
        return (start,ziel) in kanten or (ziel,start) in kanten
    
    
