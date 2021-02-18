'''
Un'azienda vende prodotti in tutta Italia e la rete di vendita è suddivisa 
in quattro zone: Nord, Centro, Sud e Isole. Dopo aver acquisito in un array 
il fatturato nelle quattro zone, calcola:
- il totale del fatturato;
- i valori in percentuale delle vendite nelle quattro zone rispetto al totale
'''
zone = ["al Nord", "nel Centro", "al Sud", "nelle Isole"]
fatturato = []
for e in zone:
    print("-", e)
    valore = int(input("Qual è stato il fatturato? "))
    fatturato.append(valore)

print()
print("Il fatturato totale è stato", sum(fatturato), "€")

for e in zone:
    print("-", e)
    perc = round(fatturato[zone.index(e)] * 100 / sum(fatturato), 2)
    print("Il fatturato è del", perc, "%")