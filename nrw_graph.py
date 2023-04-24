import networkx as nx

class nrw_graph (nx.Graph):
    
    def __init__(self):
        '''
            Es wird ein leerer Graph erzeugt
            
            Die Knoten können bereits Marken (beliebigen Typs) und boolsche Flaggen benutzen, 
            jedoch kann man weitere beliebige Attribute hinzufügen.
            
            Die Kanten können bereits Marken (beliebigen Typs), Farben und Gewichte ‚benutzen, 
            jedoch kann man weitere beliebige Attribute hinzufügen.
           
        '''
        super().__init__()
            
#########################################
    
## Zunächst einige Funktionen für Knoten:
    
    def fuegeKnotenHinzu(self, knoten, **args):
        '''
            ein neuer Knoten (ggf. mit weiteren Attributen) wird dem Graphen hinzugefügt.
        '''
        self.add_node(knoten, **args)
        
    def alleKnoten(self):
        '''
            liefert eine Liste aller Knoten.
        '''
        return list(self.nodes())
    
    def getKnotenAttribut(self, node, attr):
        '''
            liefert den durch 'attr' spezifizierten 
            Attribut-Wert des Knotens.
        '''
        assert self.knotenExists (node) , f"Knoten {node} gibt es nicht!"
        assert self.knotenHatAttribut(node, attr), f"Knoten {node} hat kein Attribut {attr}"
        
        return self.nodes[node][attr]
        
    def setKnotenAttribut(self, node, attrName, attrWert):
        '''
            Der angegebene Knoten erhält
            unter dem angegebenen AttributNamen
            den angegebenen Wert.
            
            Ggf. wird ein neues Attribut mit dem
            angegebenen Wert erzeugt.
        '''
        assert self.knotenExists (node) , f"Knoten {node} gibt es nicht!"

        self.nodes[node][attrName] = attrWert
        
    def getKnotenMitAttribut(self, attr):
        return nx.get_node_attributes(self,attr)
    
    def knotenHatAttribut(self, node, attr):
        dic = self.getKnotenMitAttribut(attr)
        return node in dic
    
    def knotenExists(self, node):
        alle = self.alleKnoten()
        return node in alle
        
# Beispielhaft werden hier Knoten 
# mit dem Attribut 'marke' und 
# einer (boolschen) Flagge versehen.

    def markiereKnoten(self, node, marke):
        '''
            die Marke des angegebenen Knoten wird gesetzt.
        '''
        self.setKnotenAttribut(node, 'marke', marke)
        
    def getKnotenMarke(self, node):
        '''
            die Markierung des angegebenen Knoten wird geliefert.
        '''
        return self.getKnotenAttribut(node, 'marke')

    def flagKnoten(self, node):
        '''
            der angegebene Knoten bekommt die (boolsche) Flagge "True"
        '''
        self.setKnotenAttribut(node, 'flagge', True)
        
    def deflagKnoten(self, node):
        '''
            der angegebene Knoten bekommt die (boolsche) Flagge "False"
        '''
        self.setKnotenAttribut(node, 'flagge', False)
        
    def knotenHatFlag(self, node):
        '''
            Es wird True geliefert genau dann,
            wenn der angegebene Knoten den
            Flaggenwert True hat.
        '''
        return self.getKnotenAttribut(node, 'flagge') == True

# Und einige Funktionen für Kanten: 

    def fuegeKanteHinzu(self, start, ziel, **args):
        '''
            eine neue Kante (ggf. mit weiteren Attributen) 
            zwischen den angegebenen Knoten wird dem Graphen hinzugefügt.
            
            Die Endknoten werden ggf. neu erzeugt.
        '''
        self.add_edge(start, ziel, **args)
        
    def alleKanten(self):
        '''
            liefert eine Liste aller Kanten.
        '''
        return self.edges()

    def getKantenAttribut(self, start, ziel, attr):
        '''
            liefert den durch 'attr' spezifizierten Attribut-Wert der Kante
        '''

        assert self.knotenExists (start) , f"Knoten {start} gibt es nicht!"
        assert self.knotenExists (ziel) , f"Knoten {ziel} gibt es nicht!"
        assert self.kanteExists (start, ziel), f"Kante {start} - {ziel} gibt es nicht!"
        assert self.kanteHatAttribut (start, ziel, attr), f"Kante {start} - {ziel} hat kein Attribut {attr}!"

        return self.edges[start, ziel][attr]
        
    def setKantenAttribut(self, start, ziel, attrName, attrWert):
        
        assert self.knotenExists (start) , f"Knoten {start} gibt es nicht!"
        assert self.knotenExists (ziel) , f"Knoten {ziel} gibt es nicht!"
        assert self.kanteExists (start, ziel), f"Kante {start} - {ziel} gibt es nicht!"

        self.edges[start, ziel][attrName] = attrWert
        
    # Die folgenden Funktionen geben der Kante
    # eine Farbe, ein Gewicht und eine Marke.
    # 
    # Falls die Kante bereits ein solches Attribut bereits besitzt, 
    # wird der alte Wert überschrieben.

    def faerbeKante(self, start, ziel, farbe):
        '''
            Die angegebene Kante wird mit der angegebenen Farbe gefärbt.
        '''

        self.setKantenAttribut(start, ziel,'farbe',farbe)
        
    def markiereKante(self, start, ziel, marke):
        '''
            Die angegebene Kante wird mit der angegebenen Marke versehen.
        '''
        self.setKantenAttribut(start, ziel,'marke',marke)
        
    def gewichteKante(self, start, ziel, gewicht):
        '''
            Die angegebene Kante wird mit dem angegebenen Gewicht versehen.
        '''

        self.setKantenAttribut(start, ziel,'gewicht',gewicht)

    # Die eingetragenen Werte können ausgelesen werden:   
    
    def kantenFarbe(self, start, ziel):
        '''
            liefert die Farbe der Kante, sofern vorhanden; ansonsten "?"
        '''

        return self.getKantenAttribut(start, ziel, 'farbe')

    def kantenGewicht(self, start, ziel):
        '''
            liefert das Gewicht der Kante, sofern vorhanden; ansonsten "?"
        '''

        return self.getKantenAttribut(start, ziel, 'gewicht')

    def kantenMarke(self, start, ziel):
        '''
            liefert die Marke der Kante, sofern vorhanden; ansonsten "?"
        '''

        return self.getKantenAttribut(start, ziel, 'marke')
    
    def getKantenMitAttribut(self, attr):
        return nx.get_edge_attributes(self,attr)
    
    def kanteHatAttribut(self, start, ziel, attr):
        dic = self.getKantenMitAttribut(attr)
        return (start, ziel) in dic or (ziel, start) in dic
    
    def kanteExists(self, start, ziel):
        kanten = self.alleKanten()
        return (start,ziel) in kanten or (ziel,start) in kanten
    
    
