import math
import time
import sympy as sp # sympy è una libreria che permette di eseguire calcoli simbolici e risolvere equazioni matematiche in modo analitico

# Risolve equazioni lineari e polinomiali di qualsiasi grado (es. x^2 - 5x + 6 = 0)
def eq_linerari_qualsiasi_grado():
    print("Inserisci l'equazione (es. x**2 - 5*x + 6 = 0 oppure x^2 - 4).")
    eq_input = input("Equazione: ").replace('^', '**')
    try:
        if "=" in eq_input:
            lhs, rhs = eq_input.split("=")
            equazione = sp.Eq(sp.sympify(lhs), sp.sympify(rhs))
        else:
            equazione = sp.Eq(sp.sympify(eq_input), 0)
        # Trova automaticamente le variabili nell'equazione
        vars = equazione.free_symbols
        soluzioni = sp.solve(equazione, list(vars) if vars else sp.symbols('x'))
        print(f"Le soluzioni dell'equazione sono: {soluzioni}")
    except Exception as e:
        print(f"Errore nella risoluzione: {e}")
    print()
    esci_o_ricomincia()

# Risolve equazioni fratte, dove l'incognita compare al denominatore, escludendo automaticamente i valori non validi
def eq_fratte_qualsiasi_grado():
    # SymPy gestisce automaticamente le equazioni fratte escludendo i valori che annullano il denominatore
    eq_linerari_qualsiasi_grado()
    print()
    esci_o_ricomincia()

# Risolve disequazioni lineari e di grado superiore (es. x^2 - 4 > 0) fornendo l'intervallo delle soluzioni
def diseq_lineari_qualsiasi_grado():
    print("Inserisci la disequazione (es. x^2 - 4 > 0). Usa >, <, >=, <=")
    diseq_input = input("Disequazione: ").replace('^', '**')
    try:
        disequazione = sp.sympify(diseq_input)
        # Trova automaticamente la variabile
        vars = disequazione.free_symbols
        soluzione = sp.reduce_inequalities(disequazione, list(vars)[0] if vars else sp.symbols('x'))
        print(f"La soluzione della disequazione è: {soluzione}")
    except Exception as e:
        print(f"Errore nella risoluzione: {e}")
    print()
    esci_o_ricomincia()

# Risolve disequazioni fratte analizzando il segno del rapporto tra numeratore e denominatore
def diseq_fratte_qualsiasi_grado():
    # La funzione reduce_inequalities gestisce correttamente anche le forme fratte
    diseq_lineari_qualsiasi_grado()
    print()
    esci_o_ricomincia()

# Permette di risolvere sistemi composti da più equazioni con più variabili (es. x + y = 5)
def sistemi_eq():
    print("Risolutore di sistemi di equazioni.")
    vars_input = input("Inserisci le variabili separate da spazio (es. x y): ").split()
    symbols = sp.symbols(vars_input)
    eqs_input = input("Inserisci le equazioni separate da virgola (es. x+y=5, x-y=1): ").replace('^', '**')
    try:
        lista_eq = []
        for eq_str in eqs_input.split(','):
            if "=" in eq_str:
                lhs, rhs = eq_str.split("=")
                lista_eq.append(sp.Eq(sp.sympify(lhs), sp.sympify(rhs)))
            else:
                lista_eq.append(sp.Eq(sp.sympify(eq_str), 0))
        soluzioni = sp.solve(lista_eq, symbols)
        print(f"Le soluzioni del sistema sono: {soluzioni}")
    except Exception as e:
        print(f"Errore nella risoluzione del sistema: {e}")
    print()
    esci_o_ricomincia()
    
# Risolve sistemi di disequazioni a una singola variabile, trovando l'intersezione delle soluzioni delle singole disequazioni
def sistemi_diseq():
    print("Risolutore di sistemi di disequazioni (singola variabile).")
    var_name = input("Inserisci la variabile (es. x): ")
    x = sp.symbols(var_name)
    diseqs_input = input("Inserisci le disequazioni separate da virgola (es. x>0, x<5): ").replace('^', '**')
    try:
        lista_diseq = [sp.sympify(d.strip()) for d in diseqs_input.split(',')]
        soluzione = sp.reduce_inequalities(lista_diseq, x)
        print(f"La soluzione del sistema di disequazioni è: {soluzione}")
    except Exception as e:
        print(f"Errore nella risoluzione del sistema: {e}")
    print()
    esci_o_ricomincia()
  
# Mostra l'interfaccia principale del programma, il menu dei tool disponibili e gestisce lo smistamento delle scelte
def introduzione_programma():
    print("Benvenuto nel calcolatore di equazioni e disequazioni di primo grado e superiore lineari e fratte e di sistemi")
    print("In questo programma è possibile risolvere equazioni e disequazioni di qualsiasi grado sia lineari che fratte ed è possibile risolvere anche i sistemi")
    print()
    while True:
        try:
            print("""Sono disponibili i seguenti tool in questo programma:\n
            1) Risolutore di equazioni lineari di qualsiasi grado\n
            2) Risolutore di equazioni fratte di qualsiasi grado\n
            3) Risolutore di disequazioni lineari di qualsiasi grado\n
            4) Risolutore di disequazioni fratte di qualsiasi grado\n
            5) Risolutore di sistemi di equazioni\n
            6) Risolutore di sistemi di disequazioni\n
            7) Esci e termina il programma del calcolatore\n""")
            tool_scelto=int(input("Selezionare il tool più adatto alle proprie esigenze (scrivere il numero associato al tool): "))
            print()
            print(f"È stato selezionato il tool numero {tool_scelto}")
            match tool_scelto:
                case 1:
                    print("Il tool in questione permette di risolvere le equazioni lineari di qualsiasi grado")
                    eq_linerari_qualsiasi_grado()
                case 2:
                    print("Il tool in questione permette di risolvere le equazioni fratte di qualsiasi grado")
                    eq_fratte_qualsiasi_grado()
                case 3:
                    print("Il tool in questione permette di risolvere le disequazioni lineari di qualsiasi grado")
                    diseq_lineari_qualsiasi_grado()
                case 4:
                    print("Il tool in questione permette di risolvere le disequazioni fratte di qualsiasi grado")
                    diseq_fratte_qualsiasi_grado()
                case 5:
                    print("Il tool in questione permette di risolvere i sistemi di equazioni")
                    sistemi_eq()
                case 6:
                    print("Il tool in questione permette di risolvere i sistemi di disequazioni")
                    sistemi_diseq()
                case 7:
                    print("Questa opzione permette di uscire e quindi di terminare (chiudere) questo programma in esecuzione")
                    time.sleep(1)
                    exit()
                case _:
                    print("Tool selezionato non valido. Il numero inserito nella scelta del tool non corrisponde a nessun tool esistente. Riprovare quindi inserendo un numero compreso tra 1 e 7.")
        except ValueError:
            print("Il tool indicato nella scelta non è valido poichè non è esistente. Assicurarsi di digitare un numero intero tra quelli elencati sopra.")

# Gestisce la logica di chiusura del programma o il ritorno al menu principale in base all'input dell'utente
def esci_o_ricomincia():
    pulsante_premuto=input("Premere Q (quit) o E (exit) per uscire, altrimenti premere qualsiasi altro pulsante per rieseguire il programma dall'inizio: ").strip().upper()
    if pulsante_premuto=="E" or pulsante_premuto=="Q":
        print("Il programma verrà chiuso a momenti...")
        time.sleep(2)
        # Termina definitivamente l'esecuzione del programma e chiude il processo
        exit()
    else:
        print("Tra poco il programma verrà eseguito nuovamente...")
        time.sleep(2)
        print()
        introduzione_programma()

# Funzione di avvio che richiama la logica principale del programma
def main():
    introduzione_programma()
    
# Punto di ingresso del codice: assicura che il programma parta solo se il file viene eseguito direttamente
if __name__=="__main__":
    main()