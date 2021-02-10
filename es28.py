'''
I nomi delle città e i corrispondenti Codici di Avviamento Postale (CAP) vengono inseriti da tastiera 
e memorizzati in un dizionario, dove il CAP è la chiave. Fornito poi da tastiera il nome di una città, 
costruisci un programma che visualizzi il suo CAP oppure un messaggio nel caso la città non sia compresa 
nell’ elenco. Analogamente, fornendo il CAP restituisce il nome della città oppure un messaggio di errore.
'''
d = {}

def trova_chiave(dicti, val):
    trovate = []
    for chiave in dicti:
        if d[chiave] == val:
            trovate.append(chiave)
    return trovate

print("Inserisci STOP quando hai finito")
while True:
    CAP = input("Qual è il CAP? ").upper()
    citta = input("Qual è la città? ").upper()
    if CAP == "STOP" or citta == "STOP":
        break
    else:
        d[CAP] = citta

print(d)

citta = input("Dimmi una città e ti dirò il CAP: ").upper()
if citta in d.values():
    print("Il CAP è", trova_chiave(d, citta))
else:
    print("Il CAP che hai inserito non è presente")

CAP = input("Dimmi un CAP e ti dirò la città ").upper()
if CAP in d.keys():
    for chiave in d.keys():
        if CAP == chiave:
            print("La città è", d[CAP])
else:
    print("La città che hai inserito non è presente")
        