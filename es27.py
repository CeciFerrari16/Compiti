'''
Organizza con un dizionario la rubrica con i nomi delle persone e i rispettivi numeri telefonici.
Fornito poi il nome della persona, il programma visualizza il suo numero di telefono oppure un messaggio
di errore nel caso la persona non sia presente nell'elenco
'''
rubrica = {
    "marco" : 438749630,
    "figaro" : 5748938690,
    "rodrigo" : 3323892374
}

print(", ".join(rubrica.keys()))
nome = input("Di chi vuoi sapere il numero di telefono?")

if nome in rubrica:
    print("Il suo numero è", rubrica[nome.lower()])
else:
    print("Il nome non è presente in rubrica")