'''
Costrusci un dizionario ottenuto da quello dell'esercizio precedente invertendo il ruolo di chiave e valore.
Usa il nuovo dizionario per trovare il nome della nazione, noto il nome della capitale.
'''
nazione = ["Italia", "Australia", "Belgio", "Brasile", "Corea del Sud", "Danimarca", "Francia", "Irlanda", "Regno Unito"]
capitale = ["Roma", "Canberra", "Bruxelles", "Brasilia", "Seul", "Copenaghen", "Parigi", "Dublino", "Londra"]
d = {}

capitale_M = []
for e in capitale:
    capitale_M.append(e.upper())

for n in range(len(nazione)):
    d[capitale_M[n]] = nazione[n]

l = ", ".join(capitale)
print(l)

capitale_user = input("Di quale capitale vuoi sapere la nazione? ").upper()

if capitale_user in capitale_M:
    print(d[capitale_user])
else:
    print("La nazione che hai scritto non è presente nell'elenco.")