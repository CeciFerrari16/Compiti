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