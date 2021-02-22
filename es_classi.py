'''
ES 1) Crea una classe Atleta per rappresentare le informazioni su un giocatore. 
La classe deve contenere un attributo booleano chiamata visitaMedica.
ES 2) Aggiungi alla classe Atleta un metodo per assegnare all'atleta il nome della squadra dove gioca.
ES 3) Aggiungi alla classe Atleta un metodo chiamato effettua_visita che ponga l'attributo 
visitaMedica uguale a True.
ES 4) Aggiungi alla classe Atleta un metodo per visualizzare i dati del giocatore.
'''
class Atleta: # Creo la classe
    def __init__(self, name, squadra, visitaMedica = False): # inializzazione dell'istanza
        self.name = name
        self.squadra = squadra
        self.visitaMedica = visitaMedica
        print("Il giorno della sua visita medica: ", visitaMedica)

    def squadra_info(self): # accetta 0 argomenti, ma devo passargli self
        print("Gioco nella squadra:", self.squadra) # non RESTITUISCE niente

    def info(self):
        print("Dati del giocatore:", self.name)
    
    def effettua_visita(self):
        self.visitaMedica = True
        if self.visitaMedica == True:
            print("Il giocatore ha fatto la visita medica")
        else:
            print("Qualcosa non va")

name_player1 = input("Qual è il nome dell'Atleta? ")
sq_player1 = input("Qual è il nome della sua squadra? ")
day = input("Che giorno ha la visita? ")
print()
player1 = Atleta(name_player1, sq_player1, day)
player1.info()
player1.squadra_info()
player1.effettua_visita()

name_player2 = input("Qual è il nome dell'Atleta? ")
sq_player2 = input("Qual è il nome della sua squadra? ")
print()
player2 = Atleta(name = name_player2, squadra = sq_player2)
player2.info()
player2.squadra_info()