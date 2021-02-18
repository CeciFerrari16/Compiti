'''
Scrivi un programma che legga un reddito da tastiera e calcoli 
l'importo dell'imposta sul reddito e la tassazione media
'''
limiti = [15000, 28000, 55000, 75000, 10**12]
aliquota = [23, 27, 38, 41, 43]
d = {}

def cal_imposta(n_aliquota):
    if n_aliquota == 0:
        scaglione = limiti[n_aliquota] * aliquota[n_aliquota] / 100
    else:
        scaglione = (limiti[n_aliquota] - limiti[n_aliquota - 1]) * aliquota[n_aliquota] / 100
    return scaglione

def imposte_prima(index):
    count = 0
    for n in range(index):
        count = count + cal_imposta(n)
    return count

for n in range(len(limiti)):
    if n == 0:
        d[limiti[0]] = (0, 0, aliquota[0])
    else:
        d[limiti[n]] = ((limiti[n - 1]), imposte_prima(n), aliquota[n])

print(d)

reddito = int(input("Inserisci il tuo reddito: "))

def indice(reddito):
    if reddito <= limiti[0]:
        index = 0
    elif reddito > limiti[0] and reddito <= limiti[1]:
        index = 1
    elif reddito > limiti[1] and reddito <= limiti[2]:
        index = 2
    elif reddito > limiti[2] and reddito <= limiti[3]:
        index = 3
    else:
        index = 4
    return index

imposta = d[limiti[indice(reddito)]]
val_prec = d[limiti[indice(reddito)]]
importo = imposta[1] + (reddito - val_prec[0]) * aliquota[indice(reddito)] / 100

print("L'importo dell'imposta sul reddito è", importo)
print("La tassazione media è", round(importo / reddito * 100, 2), "%")