'''
Scrivi un programma che data in ingresso una lista A contenete n parole, restituisca 
in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A
''' 
count = 0 
A = []
B = []
print("Ti chiederò delle parole da aggiungere alla lista A.")
print("Scrivi 'STOP' quando hai finito")
while True:
    parola = input("Scrivi una parola: ")
    if parola != "STOP":
        A.append(parola)
    else:
        break

for n in A:
    lungh = len(A[count])
    B.append(lungh)
    count += 1

print(A)
print(B)