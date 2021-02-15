'''
Organizza in una struttura di dati i valori degli occupati negli ultimi dieci anni. 
Utilizza un dizionario, assegnando il ruolo di chiave all'anno. Inserisci i dati 
da tastiera e memorizzali nel contenitore. Calcola poi il valore medio dei dieci anni 
e visualizzane il risultato.
'''
d = {}
n_anni = int(input("Quanti valori vuoi inserire? "))
for n in range(n_anni):
    anno = input("Inserisci l'anno: ")
    occupati = int(input("Inserisci il valore degli occupati: "))
    d[anno] = occupati
print(d)

media = sum(d.values()) / len(d.values())
print("Il valore medio degli occupanti è", round(media, 1) )
