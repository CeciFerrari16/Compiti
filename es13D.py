'''
Acquisisci da tastiera un elenco di parole, memorizzandole in una lista, finchè
l'utente segnala la fine dell'inserimento con un asterisco *. Visualizza alla fine il
numero delle parole memorizzate. Ordina alfabeticamente la lista delle parole 
e visualizzala, ordinata in modo crescente e decrescente.
'''
lista = []
print("Inserisci * quando hai finito")

while True:
    parola = input("Inserisci una parola: ").lower()
    if parola == "*":
        break
    else:
        lista.append(parola)

print("Il numero delle parole è", len(lista))

lista.sort()
print("La lista ordinata in modo crescente è", lista)
lista.reverse()
print("La lista ordinata in modo descrescente è", lista)