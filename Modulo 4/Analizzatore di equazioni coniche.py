import time
import numpy as np
import matplotlib.pyplot as plt

def casistiche_equazione():
    global status_conica
    # Casistica dell'ellisse e della circonferenza
    if (A > 0 and B > 0 and C == 1) or (A < 0 and B < 0 and C == -1):
        valore_assoluto_A=abs(A)
        valore_assoluto_B=abs(B)
        if valore_assoluto_A>valore_assoluto_B:
            print(f"L'equazione in questione riguarda un'elisse orizzontale, perchè |A| ({valore_assoluto_A}) > |B| ({valore_assoluto_B}) nella formula")
            status_conica="elisse orizzontale"        
        elif valore_assoluto_A<valore_assoluto_B:
            print(f"L'equazione in questione riguarda un'elisse verticale, perchè |A| ({valore_assoluto_A}) < |B| ({valore_assoluto_B}) nella formula")
            status_conica="elisse verticale"
        else:
            print(f"L'equazione in questione riguarda una circonferenza, perchè |A| ({valore_assoluto_A}) = |B| {valore_assoluto_B} nella formula")
            status_conica="circonferenza"
        disegno_conica()
    # Casistica dell'iperbole
    elif A*B<0 and (C==1 or C==-1):
        if A>0:
            if C==1:
                print(f"L'equazione in questione riguarda una iperbole orizzontale, perchè C = 1, A ({A}) > 0 e B ({B}) < 0 nella formula")
                status_conica="iperbole orrizzontale"
            else:
                print(f"L'equazione in questione riguarda una iperbole verticale, perchè C = -1, A ({A}) > 0 e B ({B}) < 0 nella formula")
                status_conica="iperbole verticale"
        else:
            if C==1:
                print(f"L'equazione in questione riguarda una iperbole verticale, perchè C = 1, A ({A}) < 0 e B ({B}) > 0 nella formula")
                status_conica="iperbole verticale"
            else:
                print(f"L'equazione in questione riguarda una iperbole orizzontale, perchè C = -1, A ({A}) < 0 e B ({B}) > 0 nella formula")
                status_conica="iperbole orrizzontale"
        disegno_conica()
    # Casistica della conica inesistente  
    else:
        print("La conica non può esistere in quanto non rispetta nessuna delle condizioni possibili affinchè possa trattarsi di una ellisse, iperbole o circonferenza")           
    esci_o_ricomincia()
    
def equazione_canonica():
    formula_equazione_canonica=input(f"L'equazione canonica finale quindi è: x^2/{A} + y^2/{B} = {C}? (rispondere solo con S/N): ").upper()
    if formula_equazione_canonica=="S":
        print("È stata scelta la risposta S, quindi a breve sarà possibile sapere se si tratta di una circonferenza, ellisse o di un iperbole")
        formula_equazione_canonica_finale=f"x^2/{A} + y^2/{B} = {C}"
        time.sleep(2)
        casistiche_equazione()
    elif formula_equazione_canonica=="N":
        print("È stata scelta la risposta N. Sarà quindi possibile reinserire i valori di A, B e C, a patto di conoscere tutti e tre i valori.")
        richiesta_parametri_input()
    else:
        print("Risposta non valida. È possibile rispondere solo con S/N. Verrà quindi comunque riformulata la domanda e sarà possibile dare una risposta diversa")
        equazione_canonica()
    
def richiesta_parametri_input():
    global A,B,C
    while True:
        try:
            A=float(input("Inserire il valore di A che si desidera: "))
            break
        except ValueError:
            print("Il valore di A inserito non è corretto, sarà possibile reinserire il valore con uno corretto (inserire solo numeri di qualsiasi tipo, non lettere o altro)")
    while True:
        try:
            B=float(input("Inserire il valore di B che si desidera: "))
            break
        except ValueError:
            print("Il valore di B inserito non è corretto, sarà possibile reinserire il valore con uno corretto (inserire solo numeri di qualsiasi tipo, non lettere o altro)")
    C=0
    while C!=1 and C!=-1:
        while True:
            try:
                C=int(input("Inserire il valore di C che si desidera (il valore di C può essere pari solo a 1 o a -1, ogni altro valore immesso non sarà accettato dal programma): "))
                break
            except ValueError:
                print("Il valore di C inserito non è corretto, sarà possibile reinserire il valore con uno corretto (inserire solo i numeri 1 o -1, non lettere o altro)")   
        if C!=1 and C!=-1:
            print("Il valore di C inserito non è corretto, sarà possibile reinserire il valore con uno corretto (il valore di C può essere pari solo a 1 o a -1, ogni altro valore immesso non sarà accettato dal programma)")
    equazione_canonica()
    
def introduzione_programma():
    print("Benvenuto nell'analizzatore di equazioni coniche!")
    print("La formula dell'equazione canonica è la seguente: x^2/A+y^2/B=C, con questa formula è possibile constatare se la conica si tratta di una circonferenza, di un ellisse o di una iperbole")
    domanda_iniziale=input("Si è conoscenza di tutti i valori numerici di A, B e C? Altrimenti non sarà possibile effettuare il calcolo della formula (rispondere solo con S/N): ").upper()
    if domanda_iniziale=="S":
        print("È stata scelta la risposta S, quindi adesso verranno chiesti tutti i tre valori di A, B e C per poter effettuare il calcolo della formula")
        richiesta_parametri_input()
    elif domanda_iniziale=="N":
        print("È stata scelta la risposta N. Spiacente, ma purtroppo se non si è a conoscenza di tutti tre i valori di A, B e C non è possibile effetuare il calcolo della formula")
        esci_o_ricomincia()
    else:
        print("Risposta non valida. È possibile rispondere solo con S/N. Il programma verrà quindi riavviato per poter inserire nuovamente una nuova risposta")
        print("Il programma verrà riavviato a momenti...")
        time.sleep(2)
        introduzione_programma()
    
def esci_o_ricomincia():
    pulsante_premuto=input("Premi Q o E per uscire, altrimenti premi qualsiasi altro pulsante per rieseguire il programma dall'inizio: ").upper()
    if pulsante_premuto=="E" or pulsante_premuto=="Q":
        print("Il programma verrà chiuso a momenti...")
        time.sleep(2)
        exit()
    else:
        print("Tra poco il programma verrà eseguito nuovamente")
        time.sleep(2)
        introduzione_programma()
        
def disegno_conica():
    x=np.linspace(-20,20,10000000)
    y_al_quadrato=B*(C-(x**2/A))
    indici_validi=y_al_quadrato>=0  
    x_validi=x[indici_validi]
    y_validi=np.sqrt(y_al_quadrato[indici_validi]) 
    plt.figure(figsize=(8, 6)) 
    plt.plot(x_validi, y_validi, label=f"x^2/{A} + y^2/{B} = {C}", color="red")
    plt.plot(x_validi, -y_validi, color="red") 
    plt.grid()
    plt.axis("equal")
    plt.xlabel("Asse x")
    plt.ylabel("Asse y")
    plt.title(f"Grafico della {status_conica}: x^2/{A} + y^2/{B} = {C}")
    plt.legend()
    plt.show(block=True)
    
introduzione_programma()