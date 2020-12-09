'''
Scrivi un programma a cui viene passata una parola e riconosce se si tratta di un palindromo oppure meno.
'''
print("Posso riconoscere se una parola è un palindromo")

parola = input("Inserisci una parola: ")

palindromo = parola[::-1] # sintassi slice
if parola == palindromo:
    print("La parola è un palindromo")
    print(palindromo, parola)
else:
    print("La parola non è un palindromo")


'''
indice = (len(parola) -1) # '-1' perchè l'indice inizia da 0
palindromo = ""

while indice >= 0:
    palindromo += parola[indice]
    indice -= 1
if palindromo == parola:
    print("La parola è un palindromo")
else:
    print("La parola non è un palindromo")
'''
