'''
Organizza con un dizionario i dati sui conti correnti bancari con un numero del conto e saldo. Fornito poi il numero 
di conto, il programma visualizza il saldo oppure un messaggio nel caso in cui il conto non sia presente nella mappa.
'''
conti = {
    "00" : 34060,
    "01" : 600000,
    "02" : 803458,
    "03" : 3450938,
    "04" : 943000
}

print(list(conti))
numero_conto = input("Qual è i numero del conto? ")

if numero_conto in conti:
    print("Il saldo è", conti[numero_conto])
else:
    print("Siamo spiacenti, questo numero di conto non è presente")