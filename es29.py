'''
Scrivi un programma che legga un reddito da tastiera e calcoli 
l'importo dell'imposta sul reddito e la tassazione media
'''
reddito = int(input("Inserisci il tuo reddito: "))
limiti = [15000, 28000, 55000, 75000, 1000000000000]
aliquota = [23, 27, 38, 41, 43]

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

def cal_imposta(n_aliquota):
    if n_aliquota == 0:
        scaglione = limiti[n_aliquota] * aliquota[n_aliquota] / 100
    else:
        scaglione = (limiti[n_aliquota] - limiti[n_aliquota - 1]) * aliquota[n_aliquota] / 100
    return scaglione

def imposte_prima(indice):
    if indice == 0:
        pagare = 0
    elif indice == 1:
        pagare = cal_imposta(0)
    elif indice == 2:
        pagare = cal_imposta(0) + cal_imposta(1)
    elif indice == 3:
        pagare = cal_imposta(0) + cal_imposta(1) + cal_imposta(2)
    else:
        pagare = cal_imposta(0) + cal_imposta(1) + cal_imposta(2) + cal_imposta(3)
    return pagare

def scaglioni_prima(indice):
    if indice == 0:
        prec_scaglioni = reddito - 0
    elif indice == 1:
        prec_scaglioni = reddito - limiti[0]
    elif indice == 2:
        prec_scaglioni = reddito - limiti[1]
    elif indice == 3:
        prec_scaglioni = reddito - limiti[2]
    else:
        prec_scaglioni = reddito - limiti[3]
    return prec_scaglioni

if reddito < limiti[4]:
    imposta = imposte_prima(indice(reddito)) + scaglioni_prima(indice(reddito)) * aliquota[indice(reddito)] / 100   
else:
    print("Il valore che hai inserito è oltre i parametri")

print("L'importo dell'imposta sul reddito è", imposta)
print("La tassazione media è", round(imposta / reddito * 100, 2), "%")