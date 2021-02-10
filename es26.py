'''
Con riferimento al dizionario del problema precedente (es25.py) elenca i numeri di matricola degli studenti che
hanno ottenuto una votazione superiore alla media di tutte le votazioni
'''

prova = {}
matricola = 0
top = []

for n in range(5):
    print("Matricola numero:", matricola)
    voto = int(input("Che voto ha preso? "))
    prova[matricola] = voto
    matricola += 1

lista_voti = list(prova.values())
media = sum(lista_voti) / len(lista_voti)
print(media)

lista_matricole = prova.keys()

for i in prova:
    bravo = lista_voti[i]
    if bravo > media:
        top.append(i)

print("Le matricole ccon il voto sopra la media:", top)