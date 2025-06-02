import time
import math
import matplotlib.pyplot as plt
from colorama import Fore, Style
import warnings
import random
import matplotlib.colors as mcolors

# Ignora tutti i tipi di Warning di qualsiasi libreria o di Python stesso
warnings.filterwarnings("ignore")

def luminanza(rgb):
    r, g, b=rgb
    return 0.2126*r+0.7152*g+0.0722*b

lista_colori_utilizzabili=[]
for nome, colore in mcolors.CSS4_COLORS.items():
    rgb=mcolors.to_rgb(colore)
    if luminanza(rgb)<0.85: # Più è alto il valore, più è chiaro il colore
        lista_colori_utilizzabili.append(nome)

# Salva la funzione originale di print
print_originale=print

# È una funzione che sostituisce i punti con le virgole solo per le variabili int e float
def print_modificato(*args, **kwargs):
    nuova_frase=" ".join(
        str(arg).replace(".", ",") if isinstance(arg, (int, float)) else str(arg)
        for arg in args
    )
    print_originale(nuova_frase, **kwargs)

# Sostituisce la funzione print con la versione modificata
print=print_modificato

# Salva la funzione originale di input
input_originale=input

# È una funzione che sostituisce le virgole con i punti negli input
def input_modificato(testo=""):
    return input_originale(testo).replace(",", ".")

# Sostituisce la funzione input con la versione modificata
input=input_modificato

# Imposta il font e la dimensione del font di default per tutti i testi di matplotlib
plt.rcParams["font.family"] = "Georgia"
plt.rcParams["font.size"] = 14

# Definisce gli angoli in gradi per i valori noti di seno e coseno all'interno di un dizionario con due keys_dizionario (seno e coseno)
dizionario_angoli_noti={
    "cos": {
        0.0: [90, 270],
        0.5: [60, 300],
        0.7071: [45, 315],
        0.8660: [30, 330],
        1.0: [0, 360]
    },
    "sin": {
        0.0: [0, 180, 360],
        0.5: [30, 150],
        0.7071: [45, 135],
        0.8660: [60, 120],
        1.0: [90]
    }
}

# Funzione per trovare approssimativamente il valore di un valore angoli in gradi
def trova_angolo_piu_vicino(risultato, simbolo_funzione):
    simbolo_funzione_dizionario=dizionario_angoli_noti[simbolo_funzione]
    keys_dizionario=list(simbolo_funzione_dizionario.keys())
    # Inizializza con il primo elemento
    key_dizionario_piu_vicina=keys_dizionario[0]
    differenza_minima=abs(keys_dizionario[0]-float(risultato))
    # Confronta con gli altri elementi
    for key_dizionario in keys_dizionario[1:]:
        differenza_attuale=abs(key_dizionario-risultato)
        if differenza_attuale<differenza_minima:
            key_dizionario_piu_vicina=key_dizionario
            differenza_minima=differenza_attuale
    return simbolo_funzione_dizionario[key_dizionario_piu_vicina]

def conferma_equazione_goniometrica_finale(tipologia_funzione_goniometrica, numero_risultato):
    if tipologia_funzione_goniometrica=="seno":
        simbolo_equazione_goniometrica="sin"
    elif tipologia_funzione_goniometrica=="coseno":
        simbolo_equazione_goniometrica="cos"
    if numero_risultato.is_integer():
        numero_risultato=int(numero_risultato)
    numero_risultato_stringa=str(numero_risultato).replace(".", ",")
    equazione_goniometrica_finale=simbolo_equazione_goniometrica+"(x)"+" = "+f"{numero_risultato_stringa}"
    print(f"{Fore.MAGENTA}Quindi l'equazione goniometrica con funzione {tipologia_funzione_goniometrica} finale è la seguente: {equazione_goniometrica_finale}{Style.RESET_ALL}")
    conferma_equazione_finale=str(input(f"L'equazione goniometrica con funzione {tipologia_funzione_goniometrica} finale mostrata nella riga sopra è corretta (rispondere solo con S o N)?: ")).strip().upper()
    if conferma_equazione_finale=="S":
        print(f"È stata scelta la risposta S, quindi adesso verranno calcolati tutti gli angoli della equazione goniometrica {equazione_goniometrica_finale} della funzione {tipologia_funzione_goniometrica}")
        valore_angoli=trova_angolo_piu_vicino(numero_risultato, simbolo_equazione_goniometrica)
        if len(valore_angoli)==2:
            valore_angoli_formattati=f"{valore_angoli[0]}° e {valore_angoli[1]}°"
        elif len(valore_angoli)>=3:
            valore_angoli_formattati=", ".join(f"{grado}°" for grado in valore_angoli[:-1])+" e "+f"{valore_angoli[-1]}°"
        else:
            valore_angoli_formattati=f"{valore_angoli[0]}°"
        if len(valore_angoli)==1:
            print(f"{Fore.YELLOW}Quindi l'angolo della funzione {tipologia_funzione_goniometrica} dell'equazione goniometrica {equazione_goniometrica_finale} è il seguente: {valore_angoli_formattati}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}Quindi gli angoli della funzione {tipologia_funzione_goniometrica} dell'equazione goniometrica {equazione_goniometrica_finale} sono i seguenti: {valore_angoli_formattati}{Style.RESET_ALL}")
        calcolo_prova_finale_equazione_goniometrica(numero_risultato, equazione_goniometrica_finale, valore_angoli, simbolo_equazione_goniometrica)
        while True:
            scelta_visualizzazione_grafico=str(input(f"Si desidera anche visualizzare un grafico che rappresenti graficamente gli angoli dell’equazione goniometrica {equazione_goniometrica_finale} (rispondere solo con S o N)?: ")).strip().upper()
            if scelta_visualizzazione_grafico=="S":
                print("È stata scelta la risposta S, quindi a breve si aprirà una finestra che mostrerà graficamente, sulla circonferenza goniometrica, gli angoli calcolati precedentemente dal programma")
                print(Fore.RED+"N.B.: Per uscire dalla dimostrazione grafica e continuare l'esecuzione del programma è necessario chiudere manualmente la finestra che apparirà a breve"+Style.RESET_ALL)
                time.sleep(3)
                stampa_angoli(valore_angoli, equazione_goniometrica_finale)
                break
            elif scelta_visualizzazione_grafico=="N":
                print(f"È stata scelta la risposta N, pertanto il programma non mostrerà graficamente gli angoli dell’equazione goniometrica {equazione_goniometrica_finale}, ma proseguirà con la normale esecuzione")
                break
            else:
                print("La risposta immessa alla domanda non è valida. È possibile rispondere solo con S (sì) o N (no). La domanda verrà quindi riformulata per poter inserire nuovamente una risposta diversa")
        print(f"In conclusione, si può quindi constatare che, per gli angoli {valore_angoli_formattati}, la funzione {tipologia_funzione_goniometrica} assume il valore {numero_risultato_stringa}. Di conseguenza, {Fore.MAGENTA}l’equazione goniometrica finale è: {equazione_goniometrica_finale}{Style.RESET_ALL}")
        esci_o_ricomincia()
    elif conferma_equazione_finale=="N":
        print("È stata scelta la risposta N. Il programma verrà quindi riavviato per poter inserire nuovamente una equazione goniometrica con funzione seno o coseno")
        esci_o_ricomincia()
    else:
        print("La risposta immessa alla domanda non è valida. È possibile rispondere solo con S (sì) o N (no). La domanda verrà quindi riformulata per poter inserire nuovamente una risposta diversa")
        time.sleep(2)
        conferma_equazione_goniometrica_finale(tipologia_funzione_goniometrica, numero_risultato)

def richiesta_generica_dati(tipologia_funzione_goniometrica):
    while True:
        try:
            numero_risultato=float(input(f"Inserisci il valore del numero che rappresenta il risultato della funzione {tipologia_funzione_goniometrica} (inserire solo un numero reale positivo tra 0 e 1 inclusi): "))
            if numero_risultato>=0 and numero_risultato<=1:
                print(f"Il valore immesso è accettato dal programma poichè rispetta i requisiti richiesti. Tra poco quindi sarà possibile venire a conoscenza di tutti gli angoli della funzione {tipologia_funzione_goniometrica} dell'equazione goniometrica")
                conferma_equazione_goniometrica_finale(tipologia_funzione_goniometrica, numero_risultato)
                break
            elif numero_risultato<=0 or numero_risultato>=1:
                print(f"Il valore immesso non è accettato dal programma poichè non rispetta i requisiti richiesti. Sarà quindi possibile reinserire il risultato della funzione {tipologia_funzione_goniometrica} dell'equazione goniometrica")
            else:
                break
        except ValueError:
            print("L'input immesso non è idoneo e perciò verrà riformulata la domanda al fine di poter rispondere nuovamente, è possibile solo rispondere con un numero reale positivo tra 0 e 1 inclusi")

def esci_o_ricomincia():
    pulsante_premuto=input("Premi Q o E per uscire, altrimenti premi qualsiasi altro pulsante per rieseguire il programma dall'inizio: ").strip().upper()
    if pulsante_premuto=="E" or pulsante_premuto=="Q":
        print("Il programma verrà chiuso a momenti...")
        time.sleep(2)
        exit()
    else:
        print("Tra poco il programma verrà eseguito nuovamente...")
        time.sleep(2)
        introduzione_programma()

def introduzione_programma():
    print(Fore.RED+"Benvenuto nel risolutore di semplici equazioni goniometriche!"+Style.RESET_ALL)
    print("Verranno effettuate alcune domande affinchè il programma possa risolvere l'equazione goniometrica in questione")
    scelta_funzione_goniometrica=str(input("Si desidera risolvere una equazione goniometrica con funzione seno (S) oppure coseno (C) (rispondere solo con S o C)?: ")).strip().upper()
    if scelta_funzione_goniometrica=="S":
        print("È stata scelta la risposta S, quindi adesso verrà chiesto un numero reale tra 0 e 1 inclusi, che rappresenta il risultato della funzione seno dell'equazione goniometrica")
        tipologia_funzione_goniometrica="seno"
        richiesta_generica_dati(tipologia_funzione_goniometrica)
    elif scelta_funzione_goniometrica=="C":
        print("È stata scelta la risposta C, quindi adesso verrà chiesto un numero reale tra 0 e 1 inclusi, che rappresenta il risultato della funzione coseno dell'equazione goniometrica")
        tipologia_funzione_goniometrica="coseno"
        richiesta_generica_dati(tipologia_funzione_goniometrica)
    else:
        print("La risposta immessa alla domanda non è valida. È possibile rispondere solo con S (seno) o C (coseno). Il programma verrà quindi riavviato per poter inserire nuovamente una nuova risposta")
        print("Il programma verrà riavviato a momenti...")
        time.sleep(2)
        esci_o_ricomincia()
        
def conversione_da_gradi_a_radianti(angolo):
    valore_angoli_radianti=angolo*(math.pi/180)
    return valore_angoli_radianti
        
def calcolo_prova_finale_equazione_goniometrica(numero_risultato, equazione_goniometrica_finale, valore_angoli, simbolo_equazione_goniometrica):
    print(f"Il programma sta effettuando un rapido controllo finale dei risultati ottenuti calcolando la funzione goniometrica {equazione_goniometrica_finale} sugli angoli trovati")
    print(Fore.CYAN+"L'operazione potrebbe richiedere alcuni secondi, attendere prego..."+Style.RESET_ALL)
    time.sleep(1)
    valore_funzione_goniometrica_errato=False
    if len(valore_angoli)==1:
        print("Il calcolo effettuato e il risultato ottenuto è il seguente:")
    else:
        print("I calcoli effettuati e i risultati ottenuti sono i seguenti:")
    for angolo in valore_angoli:
        valore_angolo_radianti=conversione_da_gradi_a_radianti(angolo)
        if simbolo_equazione_goniometrica=="sin":
            valore_funzione_goniometrica=math.sin(valore_angolo_radianti)
        elif simbolo_equazione_goniometrica=="cos":
            valore_funzione_goniometrica=math.cos(valore_angolo_radianti)
        funzione_goniometrica_scritta=f"{simbolo_equazione_goniometrica}({angolo}°)"
        risultato_funz_goniom_scritto=str(round(valore_funzione_goniometrica, 4)).replace(".", ",")
        confronto_valori_finale=math.isclose(valore_funzione_goniometrica, numero_risultato, abs_tol=1e-4)
        if confronto_valori_finale==True:
            print(f"{funzione_goniometrica_scritta} = {risultato_funz_goniom_scritto} → {Fore.GREEN}il risultato è corretto{Style.RESET_ALL}")
        else:
            print(f"{funzione_goniometrica_scritta} = {risultato_funz_goniom_scritto} → {Fore.RED}il risultato è un valore differente{Style.RESET_ALL} poiché, non essendo un valore semplificato, non coincide con il valore immesso inizialmente.")
            valore_funzione_goniometrica_errato=True
    if valore_funzione_goniometrica_errato==True:
        print(f"{Fore.RED}Nel controllo finale è stato calcolato un risultato differente{Style.RESET_ALL} poichè almeno un angolo, non essendo probabilmente un valore semplificato, non coincide con il valore immesso inizialmente per la funzione goniometrica {equazione_goniometrica_finale}")
        print(f"{Fore.RED}N.B.: Ciò significa che il risultato ottenuto è comunque valido, ma che l'angolo calcolato rappresenta un'approssimazione del valore immesso inizialmente (ovvero {numero_risultato}), in quanto quest'ultimo potrebbe non corrispondere esattamente a un valore goniometricamente noto o semplificato.{Style.RESET_ALL}")
    elif valore_funzione_goniometrica_errato==False:
        print(f"{Fore.GREEN}Il controllo finale ha avuto esito positivo{Style.RESET_ALL} poichè tutti gli angoli restituiscono il valore atteso della funzione goniometrica {equazione_goniometrica_finale}")
        
def stampa_angoli(angoli, equazione_goniometrica_finale):
    titolo_finestra_grafico_ang_eq_goniometrica=f"Angoli rappresentati sulla circonferenza goniometrica relativi all’equazione: {equazione_goniometrica_finale}"
    titolo_grafico_angoli_eq_goniometrica=f"Angoli rappresentati sulla circonferenza goniometrica relativi all’equazione: $\\mathbf{{{equazione_goniometrica_finale}}}$"
    finestra_stampa_angoli=plt.figure(figsize=(6, 6))
    gestione_finestra_grafico_angoli_eq_goniometrica=plt.get_current_fig_manager()
    try:
        gestione_finestra_grafico_angoli_eq_goniometrica.window.state("zoomed") # Rende la finestra più grande possibile senza metterla a schermo intero
    except:
        pass # Evita il crash su degli ambienti dove state("zoomed") non è direttamente supportato
    colore_randomico_grafico_retta=random.choice(lista_colori_utilizzabili)
    colore_randomico_grafico_punto=random.choice(lista_colori_utilizzabili)
    while colore_randomico_grafico_punto==colore_randomico_grafico_retta:
        colore_randomico_grafico_punto=random.choice(lista_colori_utilizzabili)
    ax=plt.subplot(111, polar=True)
    ax.set_theta_direction(1)
    ax.set_theta_zero_location("E")
    ax.set_rlim(0, 1)
    # Disegna la circonferenza unitaria (con raggio = 1)
    theta=[math.radians(grado) for grado in range(0, 361)]
    raggio_unitario=[1]*len(theta)
    ax.plot(theta, raggio_unitario, "k-", linewidth=1.5, zorder=1)
    for angolo in angoli:
        radianti=math.radians(angolo)
        # Retta dall'origine al punto
        ax.plot([0, radianti], [0, 1], "b--", linewidth=2, zorder=2, color=colore_randomico_grafico_retta)
        # Punto situato sopra la circonferenza, è leggermente spostato sopra alla circonferenza
        ax.plot(radianti, 1, "ro", markersize=8, zorder=3, color=colore_randomico_grafico_punto)
        # Etichetta
        ax.text(radianti, 1.05, f"{angolo}°", fontsize=11, ha="center", va="center", zorder=4, color="red")
    ax.set_rticks([])  
    ax.set_title(titolo_grafico_angoli_eq_goniometrica, va="bottom", usetex=False)
    finestra_stampa_angoli.canvas.manager.set_window_title(titolo_finestra_grafico_ang_eq_goniometrica)
    plt.show()

# Avvia il programma
def main():
    introduzione_programma()

if __name__ == "__main__":
    main()