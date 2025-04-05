import time
def confronto_tra_rette():
    print("Benvenuto sul programma di confronto tra le rette: incidenti, parallele e perpendicolari")
    numero_rette_confronto=int(input("Inserisci il numero di rette che desideri confrontare (inserisci solo un numero intero o decimale positivo o negativo): "))
    if numero_rette_confronto<=1:
        print("Impossibile eseguire un confronto con una sola retta o meno, è necessario almeno confrontare due o più rette")
        print("Tra poco il programma verrà eseguito nuovamente...")
        time.sleep(2)
        confronto_tra_rette()
    else:
        lista_valori_m=[]
        for i in range(numero_rette_confronto):
            valore_m_retta=float(input(f"Inserisci il valore del coefficente angolare (m) della retta n°{i + 1}: "))
            lista_valori_m.append(valore_m_retta)
        print("I valori dei coefficente angolari delle rette sono (in ordine di inserimento):")
        print(lista_valori_m)
        for i in range(0, numero_rette_confronto): # Ciclo for esterno da 0 a numero_rette_confronto-1
            for j in range(i+1, numero_rette_confronto): # Ciclo for interno da i+1 (j) a numero_rette_confronto-1
                if lista_valori_m[i]==lista_valori_m[j]: # Caso rette parallele
                    print(f"La retta n°{i + 1} con coefficiente angolare {lista_valori_m[i]} è parallela alla retta n°{j + 1} con coefficiente angolare {lista_valori_m[j]}")
                elif lista_valori_m[i]*lista_valori_m[j]==-1: # Caso rette perpendicolari
                    print(f"La retta n°{i + 1} con coefficiente angolare {lista_valori_m[i]} è perpendicolare alla retta n°{j + 1} con coefficiente angolare {lista_valori_m[j]}")
                else: # Caso rette incidenti
                    print(f"La retta n°{i + 1} con coefficiente angolare {lista_valori_m[i]} è incidente alla retta n°{j + 1} con coefficiente angolare {lista_valori_m[j]}")
    pulsante_premuto=input("Premi Q o E per uscire, altrimenti premi qualsiasi altro pulsante per fare un altro confronto tra rette: ").upper()
    if pulsante_premuto!="E" and pulsante_premuto!="Q":
        print("Tra poco il programma verrà eseguito nuovamente...")
        time.sleep(2)
        confronto_tra_rette()
    else:
        print("Il programma verrà chiuso a momenti...")
        time.sleep(2)
confronto_tra_rette()