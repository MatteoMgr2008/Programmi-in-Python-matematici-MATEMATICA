import time
import numpy as np
import math

# Salva la funzione originale di print
print_originale=print

# Crea una nuova funzione che sostituisce i punti con le virgole negli output
def print_modificato(*args, **kwargs):
    nuovo_testo = " ".join(str(arg).replace(".", ",") for arg in args)
    print_originale(nuovo_testo, **kwargs)

# Sostituisce la funzione print con la versione modificata
print=print_modificato

# Salva la funzione originale di input
input_originale=input

# Crea una nuova funzione che sostituisce le virgole con i punti negli input
def input_modificato(testo=""):
    return input_originale(testo).replace(",", ".")

# Sostituisce la funzione input con la versione modificata
input=input_modificato

def calcolo_log_semplificato(base,argomento):
    print(f"Il logaritmo finale semplificato è il seguente: log{trasformazione_pedice(base)}({argomento})")

def semplificazione_logaritmi(array_log,base):
    denominatore=1
    nuovo_argomento=1
    for logaritmo in array_log:
        denominatore*=math.log(logaritmo[0],base)
    for logaritmo in array_log:
        if(logaritmo[2]=="+"):
            nuovo_argomento*=math.pow(logaritmo[1],denominatore/math.log(logaritmo[0],base))
        else:
            nuovo_argomento/=math.pow(logaritmo[1],denominatore/math.log(logaritmo[0],base))
    nuovo_argomento=math.pow(nuovo_argomento,1/denominatore)
    
    # Arrotondare serve per evitare problemi di precisione
    if math.isclose(nuovo_argomento, 1, abs_tol=1e-10):
        nuovo_argomento=1
    return nuovo_argomento

def richiesta_base_e_argomento_log(array_log):
    for i, logaritmo in enumerate(array_log, 1):
        while True:
            try:
                valore_base_log=float(input(f"Inserisci il valore della base del logaritmo n° {i} su {num_log_semplificare}: "))
                if valore_base_log<=0 or valore_base_log==1:
                    print("La base del logaritmo deve essere necessariamente maggiore di 0 e diversa da 1! Verrà quindi riformulata la domanda al fine di poter rispondere nuovamente")
                else:
                    break
            except ValueError:
                print("L'input immesso non è idoneo e perciò verrà riformulata la domanda al fine di poter rispondere nuovamente, è possibile solo rispondere con un numero intero/decimale positivo (deve essere maggiore di 0 e non può essere negativo)")
        while True:
            try:
                valore_argomento_log=float(input(f"Inserisci il valore dell'argomento del logaritmo n° {i} su {num_log_semplificare}: "))
                if valore_argomento_log<=0:
                    print("L'argomento del logaritmo deve essere necessariamente maggiore di 0! Verrà quindi riformulata la domanda al fine di poter rispondere nuovamente")
                else:
                    break
            except ValueError:
                print("L'input immesso non è idoneo e perciò verrà riformulata la domanda al fine di poter rispondere nuovamente, è possibile solo rispondere con un numero intero/decimale positivo (non può però essere pari a 0 o ad un numero negativo)")
        while True:
            try:
                valore_segno_log=str(input(f"Inserisci il segno (+/- o POSITIVO/NEGATIVO o POS/NEG) del logaritmo n° {i} su {num_log_semplificare}: ")).upper()
                if valore_segno_log not in ["+", "-", "POSITIVO", "NEGATIVO", "POS", "NEG"]:
                    print("Il segno del logaritmo può essere solo + (positivo) o - (negativo)! Verrà quindi riformulata la domanda al fine di poter rispondere nuovamente")
                else:
                    break
            except ValueError:
                print("L'input immesso non è idoneo e perciò verrà riformulata la domanda al fine di poter rispondere nuovamente, è possibile solo rispondere con + (positivo) o - (negativo)!")
        array_log[i-1]=[valore_base_log, valore_argomento_log, valore_segno_log]
    # Sostituzione di "POSITIVO" o "POS" con "+"
    array_log[(array_log=="POSITIVO") | (array_log=="POS")] = "+"
    # Sostituzione di "NEGATIVO" o "NEG" con "-"
    array_log[(array_log=="NEGATIVO") | (array_log=="NEG")] = "-"
    stampa_espressione(array_log)
    while True:
        try:
            conferma_espressione_log_finale=str(input(f"L'equazione di logaritmi finale da semplificare è corretta (rispondere solo con S/N)?: ")).upper()
            if conferma_espressione_log_finale=="S":
                print("È stata scelta la risposta S. Quindi a breve si potrà visualizzare il logaritmo semplificato")
                break
            elif conferma_espressione_log_finale=="N":
                print("È stata scelta la risposta N. Sarà quindi possibile reinserire i valori dei diversi logaritmi da semplificare in unico logaritmo")
                introduzione_programma()
            else:
                print("L'input immesso non è idoneo e perciò verrà riformulata la domanda al fine di poter rispondere nuovamente, è possibile solo rispondere con S/N.")
        except Exception as e:
            # In caso di errore generale
            print("Si è verificato il seguente errore:")
            print(e)
    while True:
        try:
            base_log_comune_semplificato=float(input(f"Inserisci il valore della base univoca del logaritmo semplificato: "))
            if base_log_comune_semplificato<=0:
                print("L'argomento del logaritmo deve essere necessariamente maggiore di 0! Verrà quindi riformulata la domanda al fine di poter rispondere nuovamente")
            else:
                break
        except ValueError:
            print("L'input immesso non è idoneo e perciò verrà riformulata la domanda al fine di poter rispondere nuovamente, è possibile solo rispondere con un numero intero/decimale positivo")
    print("Adesso il programma applicherà le diverse proprietà dei logaritmi per poter semplificare i diversi logaritmi in un unico logaritmo finale")
    time.sleep(2)
    nuovo_argomento_log_semplificato=semplificazione_logaritmi(array_log, base_log_comune_semplificato)
    calcolo_log_semplificato(base_log_comune_semplificato, nuovo_argomento_log_semplificato)
    risultato=math.log(nuovo_argomento_log_semplificato, base_log_comune_semplificato)
    print(f"Il risultato dell'espressione semplificata logaritimica è il seguente: {risultato}")
    
def stampa_espressione(espressione):
    print("L'espressione finale da semplificare secondo i logaritmi inseriti precedemente è la seguente:", end="")
    for logaritmo in espressione:
        print(f" {logaritmo[2]} log{trasformazione_pedice(logaritmo[0])}({logaritmo[1]})", end="")    
    print()
    
def trasformazione_pedice(numero):
    # Converte i numeri in pedici usando la mappatura dei numeri
    pedici=str.maketrans("0123456789.", "₀₁₂₃₄₅₆₇₈₉,")
    if(numero%1==0):
        numero=int(numero)
        return str(numero).translate(pedici)
    else:
        return str(numero).translate(pedici)

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

def introduzione_programma():
    global  num_log_semplificare
    print("Benvenuto nel semplificatore di logaritmi in un unico logaritmo!")
    print("Verranno effettuate alcune domande per poter semplificare i logaritmi immessi in un unico logaritmo")
    while True:
        try:
            num_log_semplificare=int(input("Quanti logaritmi si desidera semplificare in unico logaritmo (inserire solo un numero intero positivo)?: "))
            if num_log_semplificare<=0:
                print(f"Impossibile semplificare {num_log_semplificare} logaritmi in un unico logaritmo, questo poichè sarebbe impossibile!")
                esci_o_ricomincia()
            elif num_log_semplificare==1:
                print("Impossibile semplificare 1 logaritmo in un unico logaritmo, questo poichè il logaritmo in questione è già semplificato!")
                esci_o_ricomincia()
            else:
                print(f"Adesso sarà possibile inserire il valore della base positiva e il valore dell'argomento di tutti {num_log_semplificare} logaritmi da semplificare")
                array_log_semplificare=np.zeros((num_log_semplificare, 3), dtype=object)
                richiesta_base_e_argomento_log(array_log_semplificare)
                esci_o_ricomincia()
        except ValueError:
            print("L'input immesso non è idoneo e perciò verrà riformulata la domanda al fine di poter rispondere nuovamente, è possibile solo rispondere con un numero intero positivo")

def main():
    introduzione_programma()

if __name__ == "__main__":
    main()