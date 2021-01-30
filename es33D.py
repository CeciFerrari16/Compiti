'''
Consegna file es33.py, ma uno un dizionario al posto di una lista
'''
pazienti = {}
print("Inserisci 0 quando hai finito")
count = 0
while True:
    nome = input("Inserisci il nome del partecipante: ")
    if nome != "0":
        pazienti[count] = nome
        count += 1
    else:
        break

for n in range(len(pazienti)):
    print("Il prossimo paziente è", pazienti.pop(n))
    input()