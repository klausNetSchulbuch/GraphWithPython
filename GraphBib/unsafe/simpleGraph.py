import pandas as pd
import GraphBib.unsafe.attrDirGraph as adg
# import attrDirGraph as adg

class simpleGraph (adg.attrDirGraph):
    
    def __init__(self):
        '''
            Es wird ein leerer ungerichteter Graph erzeugt.
            
            Knoten und Kanten können mit beliebigen 
            Attributen versehen werden.
           
        '''
        super().__init__()
            
#########################################
    
## Graph aus csv-Datei einlesen:

    def graphEinlesen(self, 
                      dateiname, 
                      sep = ",",
                      header = 0,
                     ):
        
        '''
            alle Kanten (und damit auch alle Knoten) 
            und die zugeh. Entfernungen werden 
            aus einer CSV-Datei eingelesen.
        '''
        df = pd.read_csv(dateiname, header = 0, names = ["Start", "Ziel", "Entfernung"])
        
        for i in df.index:
            s = df["Start"][i] 
            z = df["Ziel"][i] 
            e = df["Entfernung"][i]
            self.fuegeKnotenHinzu (s)
            self.fuegeKnotenHinzu (z)
            self.fuegeKanteHinzu (s,z)
            self.gewichteKante (s,z,e)
    
# Beispielhaft können hier Knoten 
# mit dem Attribut 'marke' versehen werden
# und als besucht markiert werden.
# Ein Knoten kann auch mit einer (boolschen) 
# Flagge versehen werden (als besucht markiert).

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
   
    # Die folgenden Funktionen erlauben es, 
    # der Kante eine Farbe und ein Gewicht zu geben.

    def faerbeKante(self, start, ziel, farbe):
        '''
            Die angegebene Kante wird mit der 
            angegebenen Farbe gefärbt.
        '''

        self.setKantenAttribut(start, ziel,'farbe',farbe)
                
    def gewichteKante(self, start, ziel, gewicht):
        '''
            Die angegebene Kante wird mit dem 
            angegebenen Gewicht versehen.
        '''

        self.setKantenAttribut(start, ziel,'gewicht',gewicht)

    # Die eingetragenen Werte können ausgelesen werden:   
    
    def getKantenFarbe(self, start, ziel):
        '''
            liefert die Farbe der Kante, sofern vorhanden; 
            ansonsten "?"
        '''

        return self.getKantenAttribut(start, ziel, 'farbe')

    def getKantenGewicht(self, start, ziel):
        '''
            liefert das Gewicht der Kante, sofern vorhanden; 
            ansonsten "?"
        '''

        return self.getKantenAttribut(start, ziel, 'gewicht')  
    