'''
Verifica se un numero è pari o dispari (un numero è pari quando il resto della divisione intera per 2 è uguale a 0)
'''

print("Con questo programma verificherò se il numero che inserisci è pari o dispari")

n = int(input("Inserisci un numero: "))

if n%2 == 0:
    print("Il numero che hai inserito è PARI!")
else:
    print("Il numero che hai inserito è DISPARI!")