'''
Scrivi un programma che a scelta dell'utente calcoli l'area di un quadrato, rettangolo, triangolo e cerchio
'''
print("Ciao! Posso calcolare l'area di alcune figure piane.")
print("Puoi scegliere tra queste: quadrato, rettangolo, triangolo, cerchio")

while True:
    scelta = input("Quale scegli? ").lower()
    if scelta == "quadrato":
        l = int(input("Qual è il lato del quadrato?"))
        area = l * l
        print("L'area del quadrato è", area)
        break
    elif scelta == "rettangolo":
        h = int(input("Qual è l'altezza del rettangolo?"))
        b = int(input("Qual è la base del rettangolo?"))
        area = b * h
        print("L'area del rettangolo è", area)
        break
    elif scelta == "triangolo":
        h = int(input("Qual è l'altezza del triangolo?"))
        b = int(input("Qual è la base del triangolo?"))
        area = (b * h) / 2 
        print("L'area del triangolo è", area)
        break
    elif scelta == "cerchio":
        r = int(input("Qual è il raggio del cerchio?"))
        area = r * r * 3.14
        print("L'area del cerchio è", area)
        break
    else:
        print("Non risulta che tu abbia scelto nessuna delle 4 opzioni.")
        risposta = input("Vuoi riprovare a scrivere? y/n ").lower()
        if risposta == "y":
            print("Va bene")
        else:
            print("Okay")
            break
