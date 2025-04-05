import math
import sys

sys.path.append("") # Assicura che Python cerchi nella directory corrente
semp_log_module=__import__("Semplificatore di logaritmi in un unico logaritmo")
semp_log=semp_log_module.semplificazione_logaritmi

def test_semplificazione_logaritmi():
    
    test_cases = [
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
    
    [[[2, 8, "+"], [4, 16, "+"], [3, 27, "-"]], 2, 4],  # log₂(8) + log₄(16) - log₃(27) = log₂(64)
    
    [[[2, 1024, "+"], [2, 16, "-"], [2, 4, "+"]], 2, 256],  # log₂(1024) - log₂(16) + log₂(4) = log₂(256)
    
    [[[2, 8, "+"], [2, 4, "+"], [3, 27, "-"], [2, 16, "+"]], 2, 64],  # log₂(8) + log₂(4) - log₃(27) + log₂(16) = log₂(512)
    
    [[[10, 10**8, "+"], [10, 10**6, "-"], [10, 10**4, "+"]], 10, 1000000],  # log₁₀(10⁸) - log₁₀(10⁶) + log₁₀(10⁴) = log₁₀(10000)
    
    [[[3, 9, "+"], [3, 27, "+"], [3, 81, "-"]], 3, 3],  # log₃(9) + log₃(27) - log₃(81) = log₃(243)
    
    [[[7, 7, "+"], [7, 7, "-"]], 7, 1],  # log₇(7) - log₇(7) = log₇(1)
    
    ]

    for i, (array_log, base, expected) in enumerate(test_cases, 1):
        result = semp_log(array_log, base)
        assert math.isclose(result, expected, abs_tol=1e-10), f"❌ Test {i} fallito: {result} ≠ {expected}"
        print(f"✅ Test {i} superato: {result} = {expected}")

# Esegue i test descritti sopra
test_semplificazione_logaritmi()