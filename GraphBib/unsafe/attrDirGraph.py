import networkx as nx

class attrDirGraph (nx.Graph):
    
    def __init__(self):
        '''
            Es wird ein leerer ungerichteter Graph erzeugt.
            
            Knoten und Kanten können mit beliebigen Attributen versehen werden.
           
        '''
        super().__init__()
            
#########################################

## Funktionen für Knoten
    
    def fuegeKnotenHinzu(self, knoten, **args):
        '''
            ein neuer Knoten (ggf. mit weiteren Attributen) 
            wird dem Graphen hinzugefügt.
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
#        assert self.knotenExists (node) , f"Knoten {node} gibt es nicht!"
#        assert self.knotenHatAttribut(node, attrName), f"Knoten {node} hat kein Attribut {attrName}"
        
        return self.nodes[node][attrName]
    
    def getKnotenAttribute(self, node):
        '''
            liefert ein Dictionary der Attribute des Knotens.
        '''
#        assert self.knotenExists (node) , f"Knoten {node} gibt es nicht!"
        
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
                
# Funktionen für Kanten: 

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
            liefert den durch 'attr' spezifizierten 
            Attribut-Wert der Kante
        '''

#        assert self.knotenExists (start) , f"Knoten {start} gibt es nicht!"
#        assert self.knotenExists (ziel) , f"Knoten {ziel} gibt es nicht!"
#        assert self.kanteExists (start, ziel), f"Kante {start} - {ziel} gibt es nicht!"
#        assert self.kanteHatAttribut (start, ziel, attr), f"Kante {start} - {ziel} hat kein Attribut {attr}!"

        return self.edges[start, ziel][attr]
        
    def setKantenAttribut(self, start, ziel, attrName, attrWert):
        '''
            Die durch start und ziel spezifizierte Kante 
            erhält für das angegebene Attribut den angegebenen Wert
        '''
        
#        assert self.knotenExists (start) , f"Knoten {start} gibt es nicht!"
#        assert self.knotenExists (ziel) , f"Knoten {ziel} gibt es nicht!"
#        assert self.kanteExists (start, ziel), f"Kante {start} - {ziel} gibt es nicht!"

        self.edges[start, ziel][attrName] = attrWert
        
    def alleNachbarknoten(self, start):
        '''
            Eine Liste der Nachbarknoten des 
            angegebenen Knoten wird geliefert
        '''
        
#        assert self.knotenExists (start) , f"Knoten {start} gibt es nicht!"
        return list(self.neighbors(start))
