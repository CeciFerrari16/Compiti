'''
Implementa l'algoritmo per il calcolo della soluzione di un'equazione di primo grado a x + b = 0.
Il processo risolutivo dipende dai valori assunti dai coefficienti a e b secondo la tabella allegata nel README.md file
'''
import fractions

a = int(input("Inserisci il valore di a: "))
b = int(input("Inserisci il valore di b: "))

if a == 0 and b == 0:
    print("L'equazione è INDETERMINATA")

elif a == 0 and b != 0:
    print("L'equazione è IMPOSSIBILE")

elif a != 0 and b == 0:
    print("La soluzione è x = 0")

else: #quando a != 0 e b != 0
    if b%a != 0: #quando la soluzione è dispari
        x = fractions.Fraction(- b , a) #frazione
        print("La soluzione è x =", x) 
    else:
        x = -(b / a)
        print("La soluzione è x =", int(x))