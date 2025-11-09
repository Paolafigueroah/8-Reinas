"""
Script para combinar los resultados de los experimentos individuales en un solo archivo.
"""

import json
import os

def combinar_resultados():
    """Combina los resultados de los experimentos en un solo archivo."""
    resultados_combinados = {
        'experimento1': {},
        'experimento2': {},
        'experimento3': {}
    }
    
    # Cargar Experimento 1
    if os.path.exists('resultados_experimento1.json'):
        with open('resultados_experimento1.json', 'r', encoding='utf-8') as f:
            exp1 = json.load(f)
            resultados_combinados['experimento1'] = exp1.get('experimento1', {})
    
    # Cargar Experimento 2
    if os.path.exists('resultados_experimento2.json'):
        with open('resultados_experimento2.json', 'r', encoding='utf-8') as f:
            exp2 = json.load(f)
            resultados_combinados['experimento2'] = exp2.get('experimento2', {})
    
    # Cargar Experimento 3
    if os.path.exists('resultados_experimento3.json'):
        with open('resultados_experimento3.json', 'r', encoding='utf-8') as f:
            exp3 = json.load(f)
            resultados_combinados['experimento3'] = exp3.get('experimento3', {})
    
    # Guardar archivo combinado
    with open('resultados_experimentos.json', 'w', encoding='utf-8') as f:
        json.dump(resultados_combinados, f, indent=2, ensure_ascii=False)
    
    print("Resultados combinados en: resultados_experimentos.json")
    print(f"  - Experimento 1: {'✓' if resultados_combinados['experimento1'] else '✗'}")
    print(f"  - Experimento 2: {'✓' if resultados_combinados['experimento2'] else '✗'}")
    print(f"  - Experimento 3: {'✓' if resultados_combinados['experimento3'] else '✗'}")

if __name__ == "__main__":
    combinar_resultados()

