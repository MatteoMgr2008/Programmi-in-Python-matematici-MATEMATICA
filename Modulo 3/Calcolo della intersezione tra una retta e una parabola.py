import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import warnings
import logging
# Eliminazione degli avvisi di tipo "UserWarning"
warnings.filterwarnings('ignore')
rcParams["font.family"] = "Roboto" # Imposta il font presente di default per i grafici
# Disabilitazione specifica dei log di Matplotlib sui font
logging.getLogger('matplotlib.font_manager').setLevel(logging.ERROR)
def calcolo_intersezione_retta_parabola():
    # Input dei coefficenti della parabola
    def coefficenti_parametri_parabola():
        global coefficente_x_parabola,coefficente_x2_parabola,coefficente_numero_parabola, formula_parabola
        coefficente_x_parabola=int(input("Inserisci il coefficente di x della parabola: "))
        coefficente_x2_parabola=int(input("Inserisci il coefficente di x^2 della parabola: "))
        coefficente_numero_parabola=int(input("Inserisci il coefficente senza la x della parabola: "))
        formula_parabola=f"{coefficente_x_parabola}x + {coefficente_x2_parabola}x^2 + {coefficente_numero_parabola}"
        print(f"Quindi la formula in forma canonica della parabola secondo i coefficenti immessi è: {formula_parabola}")
        conferma_coeffecenti_parabola=input("Premere S se la formula in forma canonica della parabola è corretta o in caso contrario premere N. Ogni risposta alternativa verrà interpretata dal programma come risposta sbagliata. ").upper()
        if conferma_coeffecenti_parabola=="S":
            print("È stata scelta la risposta S, quindi adesso verranno chiesti in input i dati dei coefficenti della retta")
            coefficenti_parametri_retta()
        elif conferma_coeffecenti_parabola=="N":
            print("È stata scelta la risposta N, quindi adesso verranno richiesti nuovamente in input i dati dei coefficenti della parabola")
            coefficenti_parametri_parabola()
        else:
            print("Risposta non valida. Verranno quindi comunque richiesti nuovamente in input i dati dei coefficenti della parabola")
        coefficenti_parametri_parabola()
    # Input dei coefficenti della retta
    def coefficenti_parametri_retta():
        global coefficente_x_retta, coefficente_numero_retta, formula_retta
        coefficente_x_retta=int(input("Inserisci il coefficente di x della retta (ossia il coefficente angolare): "))
        coefficente_numero_retta=int(input("Inserisci il coefficente senza la x della retta (ossia l'intercetta): "))
        formula_retta=f"{coefficente_x_retta}x + {coefficente_numero_retta}"
        print(f"Quindi la formula in forma canonica della retta secondo i coefficenti immessi è: {formula_retta}")
        conferma_coeffecenti_retta=input("Premere S se la formula in forma canonica della retta è corretta o in caso contrario premere N. Ogni risposta alternativa verrà interpretata dal programma come risposta sbagliata. ").upper()
        if conferma_coeffecenti_retta=="S":
            print("È stata scelta la risposta S, quindi adesso verrà effettuato il calcolo finale")
            calcolo_finale_delta()
        elif conferma_coeffecenti_retta=="N":
            print("È stata scelta la risposta N, quindi adesso verranno richiesti nuovamente in input i dati dei coefficenti della retta")
            coefficenti_parametri_retta()
        else:
            print("Risposta non valida. Verranno quindi comunque richiesti nuovamente in input i dati dei coefficenti della retta")
            coefficenti_parametri_retta()
    # Output grafico del risultato finale del delta (Δ)
    def output_grafico():
        # Generazione dei valori di x del grafico
        valori_x_grafico=np.linspace(-100,100,500)
        # Calcolo di y per la parabola
        valore_y_parabola=coefficente_x2_parabola*valori_x_grafico**2+coefficente_x_parabola*valori_x_grafico+coefficente_numero_parabola
        # Calcolo di y per la retta
        valore_y_retta=coefficente_x_retta*valori_x_grafico+coefficente_numero_retta
        # Disegna il grafico
        plt.figure(figsize=(18, 16))
        plt.plot(
                valori_x_grafico,
                valore_y_parabola,
                label="Parabola",
                color="black"
                )
        plt.plot(
                 valori_x_grafico,
                 valore_y_retta,
                 label="Retta",
                 color="red"
                 )
        # Personalizzazioni
        plt.axhline(
                    0,
                    color="black",
                    linewidth=0.5,
                    linestyle="--"
                    )
        plt.axvline(
                    0,
                    color="black",
                    linewidth=0.5,
                    linestyle="--"
                    )
        plt.legend(
            fontsize=15,
            prop={"family": "Roboto"}, # Imposta il font della legenda
            loc="upper left",
            bbox_to_anchor=(1, 1.01),
            frameon=True,
            facecolor="white",
            edgecolor="black",
            framealpha=0.7, # Imposta la trasparenza del riquadro
            shadow=True, # Aggiunge un'ombra al riquadro della legenda
            borderpad=1.2 # Aggiunge dello spazio tra il testo e il bordo
                  )
        plt.title(
                f"Intersezione tra la parabola ({formula_parabola}) e la retta ({formula_retta})",
                  fontsize=18,
                  color="red",
                  backgroundcolor="white",
                  fontweight="bold",
                  fontname="Roboto",
                  loc="center",
                  pad=30
                  )
        plt.xlabel(
            "Valori dell'asse x",
            fontsize=15,
            fontweight="light",
            fontname="Roboto",
            )
        plt.ylabel(
            "Valori dell'asse y",
            fontsize=15,
            fontweight="light",
            fontname="Roboto",
            )
        plt.grid(
            color="gray",
            linestyle="--",
            linewidth=0.5
            )
        plt.show()
    # Calcolo finale del delta (Δ)
    def calcolo_finale_delta():
        formula_calcolo_delta=(coefficente_x_retta-coefficente_x_parabola)**2-4*(-coefficente_x2_parabola)*(coefficente_numero_retta-coefficente_numero_parabola) # Formula generica per il calcolo del delta (Δ)
        print(f"Il risultato del calcolo finale del delta (Δ), secondo i parametri inseriti precedentemente, è: {formula_calcolo_delta}")
        if formula_calcolo_delta>0:
            print("Secondo i dati immessi precedentemente la retta è di tipo SECANTE")
        elif formula_calcolo_delta==0:
            print("Secondo i dati immessi precedentemente la retta è di tipo TANGENTE")
        elif formula_calcolo_delta<0:
            print("Secondo i dati immessi precedentemente la retta è di tipo ESTERNA")
        output_grafico()
        esci_o_ricomincia()
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
    # Introduzione al programma
    def introduzione_programma():
        print("Benvenuto nel calcolatore della intersezione tra una retta e una parabola")
        print("N.B.: Verranno richiesti i coefficenti di tutti i parametri della retta (solo obliqua o orizzontale) e della parabola (solo se è verticale) entrambe in forma esplicita")
        domanda_iniziale=input("La retta in questione, secondo i parametri della formula, è verticale (rispondere solo con S o N)? ").upper()
        if domanda_iniziale=="S":
            print("È stata scelta la risposta S, quindi essendo una retta verticale automaticamente è classificabile come una retta di tipo tangente")
            esci_o_ricomincia()
        elif domanda_iniziale=="N":
            print("È stata scelta la risposta N, quindi adesso verranno richiesti in input i diversi dati dei coefficenti necessari per il calcolo finale")
            coefficenti_parametri_parabola()
        else:
            print("Risposta non valida. Il programma verrà quindi riavviato per poter inserire nuovamete una nuova risposta")
            print("Il programma verrà riavviato a momenti...")
            time.sleep(2)
            introduzione_programma()
    introduzione_programma()
calcolo_intersezione_retta_parabola()