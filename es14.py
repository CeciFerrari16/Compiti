'''
Crea un programma che scriva la differenza di due numeri a e b se il loro prodotto è maggiore di 10, 
oppure la loro somma se il prodotto è minore o uguale a 10. Esegui poi il programmacon diverse 
coppie di valoroi per a e b: (-5,2), (5,-5), (10,2), (-4,-5), (5,4), (-3,-2)
'''
while True:
    a = int(input("Inserisci il numero a: "))
    b = int(input("Inserisci il numero b: "))
    if a * b > 10:
        print(a - b)
    else:
        print(a + b)

    risposta = input("Vuoi continuare? yes/no ").lower()
    if risposta == "no":
        break
    