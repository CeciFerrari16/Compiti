'''
Risolvi il problema precedente partendo da due liste che generano un dizionario con la nazione come chiave 
e la capitale come valore. Suggessivamente interroga il dizionario per visualizzare la capitale di una nazione.
'''
nazione = ["Italia", "Australia", "Belgio", "Brasile", "Corea del Sud", "Danimarca", "Francia", "Irlanda", "Regno Unito"]
capitale = ["Roma", "Canberra", "Bruxelles", "Brasilia", "Seul", "Copenaghen", "Parigi", "Dublino", "Londra"]
d = {}

for n in range(len(nazione)):
    d[nazione[n].upper()] = capitale[n]

l = ", ".join(nazione)
print(l)

nazione_user = input("Di quale nazione vuoi sapere la capitale? ").upper()

if nazione_user in d:
    print(d[nazione_user])
else:
    print("La nazione che hai scritto non è presente nell'elenco.")