'''
Crea una classe Atleta per rappresentare le informazioni su un giocatore. 
La classe deve contenere un attributo booleano chiamata visitaMedica.
Aggiungi alla classe Atleta un metodo per assegnare all'atleta il nome della squadra dove gioca.
Aggiungi alla classe Atleta un metodo chiamato effettua_visita che ponga l'attributo 
visitaMedica uguale a True.
Aggiungi alla classe Atleta un metodo per visualizzare i dati del giocatore.
'''
class Atleta:
    def __init__(self, name, visitaMedica, squadra):
        self.name = name
        self.squadra = squadra
        self.visitaMedica = int(visitaMedica)
        print("Il giorno della sua visita medica: ", visitaMedica)

    def squadra_info(self):
        print("Gioco nella squadra:", self.squadra)

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
giorno = input("Che giorno ha la visita? ")
print()
player1 = Atleta(name_player1, giorno, sq_player1)
player1.info()
player1.squadra_info()
player1.effettua_visita()