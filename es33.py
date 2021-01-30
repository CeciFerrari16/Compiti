'''
In un laboratorio di analisi i pazienti sono sottoposti a un esame specialistico secondo l'ordine di arrivo: 
scrivi il programma che consenta di registrare i nomi dei pazienti man mano che arrivano. Visualizza poi
il nome del paziente che deve essere sottoposto all'esame perchè è il primo della coda in attesa
'''
pazienti = []
print("Inserisci 0 quando hai finito")
while True:
    nome = input("Inserisci il nome del partecipante: ")
    if nome != "0":
        pazienti.append(nome)
    else:
        break

for n in range(len(pazienti)):
    print("Il prossimo paziente è", pazienti.pop(0))
    input()
