'''
Dato un elenco di nazioni contenuto in una lista e uno delle rispettive capitali in un'altra lista con lo stesso indice, 
visualizza la capitale di una nazione della quale viene fornito da tastiera il nome, segnalando con un messaggio di errore 
il caso in cui la nazione richiesta non sia compresa nell'elenco
'''
nazione = ["Italia", "Australia", "Belgio", "Brasile", "Corea del Sud", "Danimarca", "Francia", "Irlanda", "Regno Unito"]
capitale = ["Roma", "Canberra", "Bruxelles", "Brasilia", "Seul", "Copenaghen", "Parigi", "Dublino", "Londra"]

nazione_M = []
for e in nazione:
    nazione_M.append(e.upper())

l = ", ".join(nazione)
print(l)

nazione_user = input("Di quale nazione vuoi sapere la capitale? ").upper()

if nazione_user in nazione_M:
    index = nazione_M.index(nazione_user)
    print(capitale[index])
else:
    print("La nazione che hai scritto non è presente nell'elenco.")