'''
ES 5) Elenca le proprietà e i metodi della classe Prodotto
ES 6) Definisci il metodo assegna_prezzo della classe Prodotto
ES 7) Elenca proprietà e metodi della classe Motociclo
'''
class Prodotto:
    def __init__(self, brand, price):
        self.brand = brand

    def assegna_prezzo(self):
        self.price = int(input("Stabilisci il prezzo: "))
        print("Sto assegnando il prezzo") 
        
    def info(self):
        print("Il prodotto è di", self.brand)
        print("Il prezzo è", self.price)

class Motociclo(Prodotto):
    def __init__(self, name, brand, velocità, price = 0):
        super().__init__(brand, price)
        self.name = name
        self.velocità = velocità
    
    def info_moto(self):
        print("Il suo brand è", self.brand)
        print("Il suo nome è", self.name)
        print("Il prezzo è", self.price)
        print("La sua velocità è", self.velocità)

moto = Motociclo("Vasco", "Fiat", "130 km/h")
moto.assegna_prezzo()
moto.info_moto()

'''
ES 8) Crea una classe Quadrato con l'attributo lato 
    e i metodi per il calcolo del perimetro e dell'area
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

figura = Quadrato(lato = 6)
figura.perimetro()
figura.cal_area()