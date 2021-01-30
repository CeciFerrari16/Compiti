'''
Le prenotazioni per la partecipazione a un convegno sono memorizzate secondo l'ordine di arrivo. Scrivi un programma
che comprenda queste funzionalità:
- l'operazione per registare i dati dei partecipanti
- l'operazione per visualizzare i nomi dei partecipanti a cui si deve inviare una lettera di conferma: 
si tratta dei nomi dell'elenco, eliminando quelli ai quali la lettera è già stata inviata e che sono registrati 
in un apposito elenco. La funzione che produce l'elenco deve anche aggiornare l'elenco dei partecipanti ai quali 
è già stata inviata la lettera.
'''
partecipanti = []
lettera_consegnata = []
print("Inserisci 0 quando hai finito")
while True:
    nome = input("Inserisci il nome del partecipante: ")
    if nome != "0":
        partecipanti.append(nome)
        conferma = input("E'stata già inviata la lettera di conferma a questo partecipante? y/n ").lower()
        if conferma == "y":
            partecipanti.remove(partecipanti[-1])
            lettera_consegnata.append(nome) #lettera già consegnata
    else:
        break

print("Si deve inviare la lettera di conferma a", ", ".join(partecipanti))