import math
import sys
import os
import time
from colorama import Fore, Style, init

# Aggiunge il percorso del modulo "Semplificatore di logaritmi in un unico logaritmo" alla lista dei percorsi di ricerca dei moduli
sys.path.append(os.path.join("..", "Semplificatore di logaritmi in un unico logaritmo")) # Assicura che Python cerchi nella directory corretta
modulo_semplificatore_log=__import__("Semplificatore di logaritmi in un unico logaritmo")
semplificatore_log=modulo_semplificatore_log.semplificazione_logaritmi

def test_semplificazione_logaritmi():
    test_casistiche = [
    
        # Caso base
        [[[8, 8, "+"], [9, 9, "-"]], 3, 1],  # log₈(8) - log₉(9) → log₃(1) → 0

        # Sottrazione di logaritmi (divisione degli argomenti)
        [[[2, 8, "+"], [2, 4, "-"]], 2, 2],  # log₂(8) - log₂(4) = log₂(2) = 1

        # Somma di logaritmi (moltiplicazione degli argomenti)
        [[[2, 8, "+"], [2, 4, "+"]], 2, 32],  # log₂(8) + log₂(4) = log₂(32) = 5

        # Logaritmo con basi diverse
        [[[2, 8, "+"], [4, 16, "-"]], 2, 2],  # log₂(8) - log₄(16) = log₂(2) = 1

        # Logaritmi con basi diverse e argomenti arbitrari
        [[[5, 25, "+"], [10, 100, "-"]], 10, 1],  # log₅(25) - log₁₀(100) = log₁₀(1) = 0

        # Più logaritmi, somma e sottrazione
        [[[2, 8, "+"], [2, 4, "+"], [2, 16, "-"]], 2, 2],  # log₂(8) + log₂(4) - log₂(16) = log₂(2)

        # Caso limite con argomenti grandi
        [[[10, 10**6, "+"], [10, 10**3, "-"]], 10, 1000],  # log₁₀(10⁶) - log₁₀(10³) = log₁₀(1000)

        # Test con logaritmi di numeri molto piccoli
        [[[2, 0.5, "+"], [2, 8, "-"]], 2, 0.0625],  # log₂(0.5) - log₂(8) = log₂(0.0625)

        # Logaritmi che annullano l'effetto reciproco
        [[[10, 1000, "+"], [10, 1000, "-"]], 10, 1],  # log₁₀(1000) + log₁₀(1000) - log₁₀(1000) = log₁₀(1)

        # Test con logaritmi di argomenti uguali e basi uguali
        [[[2, 2, "+"], [2, 2, "+"],[2, 2, "-"]], 2, 2],  # log₂(2) + log₂(2) - log₂(2) = log₂(2)
        
        # Combinazioni complesse con basi e argomenti diversi
        [[[5, 125, "+"], [3, 27, "+"], [10, 1000, "-"]], 10, 1000],  # log₅(125) + log₃(27) - log₁₀(1000) = log₁₀(250)

        # Caso limite con zero
        [[[10, 1, "+"], [10, 1, "-"]], 10, 1],  # log₁₀(1) + log₁₀(1)= log₁₀(1)
        
        # Combinazioni di logaritmi con basi e argomenti diversi
        [[[2, 8, "+"], [4, 16, "+"], [3, 27, "-"]], 2, 4],  # log₂(8) + log₄(16) - log₃(27) = log₂(64)
        
        # Combinazioni di logaritmi con basi e argomenti diversi
        [[[2, 1024, "+"], [2, 16, "-"], [2, 4, "+"]], 2, 256],  # log₂(1024) - log₂(16) + log₂(4) = log₂(256)
        
        # Combinazioni di logaritmi con basi e argomenti diversi
        [[[2, 8, "+"], [2, 4, "+"], [3, 27, "-"], [2, 16, "+"]], 2, 64],  # log₂(8) + log₂(4) - log₃(27) + log₂(16) = log₂(512)
        
        # Combinazioni di logaritmi con basi e argomenti diversi
        [[[10, 10**8, "+"], [10, 10**6, "-"], [10, 10**4, "+"]], 10, 1000000],  # log₁₀(10⁸) - log₁₀(10⁶) + log₁₀(10⁴) = log₁₀(10000)
        
        # Combinazioni di logaritmi con basi e argomenti diversi
        [[[3, 9, "+"], [3, 27, "+"], [3, 81, "-"]], 3, 3],  # log₃(9) + log₃(27) - log₃(81) = log₃(243)
        
        # Combinazioni di logaritmi con basi e argomenti diversi
        [[[7, 7, "+"], [7, 7, "-"]], 7, 1],  # log₇(7) - log₇(7) = log₇(1)
    
    ]
    numero_test_totali=len(test_casistiche)
    
    # Contatori per i risultati dei test
    contatore_test_falliti = 0
    contatore_test_superati = 0

    # Esegue i test sui logaritmi soprastanti
    print("Esecuzione dei test sui logaritmi in corso...")
    time.sleep(2) # Simula un breve ritardo per l'esecuzione dei test
    print()
    print("Test effettuati:")
    for i, (array_log, base, risultato_previsto) in enumerate(test_casistiche, 1):
        risultato_ottenuto = semplificatore_log(array_log, base)
        if math.isclose(risultato_ottenuto, risultato_previsto, abs_tol=1e-10):
            time.sleep(1)
            print(f"{Fore.GREEN}Test {i} superato: {risultato_ottenuto} = {risultato_previsto}{Style.RESET_ALL}")
            contatore_test_superati+=1
        else:
            time.sleep(1)
            print(f"{Fore.RED}Test {i} fallito: {risultato_ottenuto} ≠ {risultato_previsto}{Style.RESET_ALL}")
            contatore_test_falliti+=1
    print()
    
    # Riepilogo finale dei test
    print("Riepilogo dei test effettuati:")
    print(f"{Fore.GREEN}N° di test sui logaritmi superati: {contatore_test_superati} di {numero_test_totali}{Style.RESET_ALL}")
    print(f"{Fore.RED}N° di test sui logaritmi falliti: {contatore_test_falliti} di {numero_test_totali}{Style.RESET_ALL}")
    print()
    
    # Verifica se tutti i test sono stati superati
    if contatore_test_superati==numero_test_totali and contatore_test_falliti==0:
        print(f"{Fore.GREEN}Tutti i test sui logaritmi effettuati hanno avuto un esito positivo e non risultano quindi esserci test falliti!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}NON tutti i test sui logaritmi effettuati hanno avuto un esito positivo e risultano quindi esserci test falliti!{Style.RESET_ALL}")
    
# Esegue i test descritti sopra
test_semplificazione_logaritmi()