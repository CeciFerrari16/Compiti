'''
I voti assegnati a 30 studenti di una classe in una prova di italiano sono memorizzati in un dizionario 
che ha per chiave la matricola, mentre il valore associato e il voto. Elenca i risultati in ordine crescente 
di voto e successivamente visualizza quali voti diversi tra loro sono stati assegnati, riducendo uno i voti uguali.
'''

prova = {}
matricola = 0

for n in range(30):
    print("Matricola numero:", matricola)
    voto = int(input("Che voto ha preso? "))
    prova[matricola] = voto
    matricola += 1

ordinato = sorted(prova.values())
print("Ecco la lista con tutti i voti:", ordinato)

for e in ordinato:
    n = ordinato.count(e)
    if n >= 2:
        ordinato.remove(e)

print("Ecco i voti diversi che sono stati dati:", ordinato)