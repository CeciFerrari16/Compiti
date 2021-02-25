'''
Deriva dalla classe Quadrato dell'es 8 una nuova classe Rettangolo aggiungendo un secondo lato
per l'altezza e riscrivendo i metodi per il calcolo del perimetro e l'area
'''
class Quadrato:
    def __init__(self, lato):
        self.lato = lato
    
    def perimetro(self):
        perimeter = 4 * self.lato
        print("Il perimetro è di", perimeter)
    
    def cal_area(self):
        area = self.lato **2
        print("L'area è di", area)

class Rettangolo(Quadrato):
    def __init__(self, lato, altezza):
        super().__init__(lato)
        self.altezza = altezza

    def perimetro(self):
        print("Il perimetro è", self.lato * 2 + self.altezza * 2)
    
    def area(self):
        print("L'area è", self.lato * self.altezza)

ret = Rettangolo(3, 7)
ret.area()
ret.perimetro()
