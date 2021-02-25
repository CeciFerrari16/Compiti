'''
Crea la classe Triangolo, la classe derivata TriangoloIsoscele e TriangoloEquilatero
'''
class Triangolo:
    def __init__(self, cat1, cat2, base):
        self.cat1 = cat1
        self.cat2 = cat2
        self.base = base
    
    def info(self): 
        print("Cateti 1 e 2:", self.cat1, self.cat2)
        print("Base:", self.base)
    
class TriangoloIsocele(Triangolo):
    def __init__(self, cat1, base):
        super().__init__(cat1, base)
        self.cat1 = cat1
    
    def info_iso(self):
        print("Lati obliqui", self.cat1)
        print("Base:", self.base)
    
class TriangoloEquilatero(TriangoloIsocele):
    def __init__(self, lato):
        self.lato = lato
    
    def info_equa(self):
        print("Lato", self.lato)

triangolo = TriangoloEquilatero("6")
triangolo.info_equa()

    
