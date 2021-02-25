'''
Data la classe Motociclo creata nel es 7, dericva la classe Ciclomotore. Aggiungi le proprietà opportune
e modifica il metodo che consente di visualizzare i valori delle proprietà
'''

class Motociclo():
    def __init__(self, brand, price = 0):
        self.brand = brand 
        self.price = price
    
    def assegna_prezzo(self):
        self.price = int(input("Stabilisci il prezzo: "))
        print("Sto assegnando il prezzo")
    
    def info(self):
        print("Il suo brand è", self.brand)
        print("Il prezzo è", self.price)

class Ciclomotore(Motociclo):
    def __init__(self, brand, velocita = "45 km/h", price = 0):
        super().__init__(brand, price)
        self.velocita = velocita
    
    def info_moto(self):
        super().info()
        print("La sua velocità è", self.velocita)
    
moto = Motociclo("Fiat")
moto.assegna_prezzo()
moto.info()

ciclo = Ciclomotore("Mercedes")
ciclo.assegna_prezzo()
ciclo.info_moto()