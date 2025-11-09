"""
Script principal que ejecuta todos los experimentos
"""

import sys
from pathlib import Path

# Agregar el directorio padre al path
sys.path.insert(0, str(Path(__file__).parent.parent))

from experimentos.experimento1_escalabilidad import experimento1_escalabilidad
from experimentos.experimento2_consistencia import experimento2_consistencia
from experimentos.experimento3_optimizacion import experimento3_optimizacion
from codigo.utils import ensure_dir
import json

# Rutas
BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = BASE_DIR / "experimentos" / "resultados_brutos"
ensure_dir(str(RESULTS_DIR))


def combinar_resultados():
    """Combina los resultados de los tres experimentos en un solo archivo."""
    resultados_combinados = {}
    
    # Cargar Experimento 1
    exp1_path = RESULTS_DIR / "exp1_resultados.json"
    if exp1_path.exists():
        with open(exp1_path, 'r', encoding='utf-8') as f:
            exp1 = json.load(f)
            resultados_combinados.update(exp1)
    
    # Cargar Experimento 2
    exp2_path = RESULTS_DIR / "exp2_resultados.json"
    if exp2_path.exists():
        with open(exp2_path, 'r', encoding='utf-8') as f:
            exp2 = json.load(f)
            resultados_combinados.update(exp2)
    
    # Cargar Experimento 3
    exp3_path = RESULTS_DIR / "exp3_resultados.json"
    if exp3_path.exists():
        with open(exp3_path, 'r', encoding='utf-8') as f:
            exp3 = json.load(f)
            resultados_combinados.update(exp3)
    
    # Guardar archivo combinado
    combined_path = RESULTS_DIR / "resultados_combinados.json"
    with open(combined_path, 'w', encoding='utf-8') as f:
        json.dump(resultados_combinados, f, indent=2, ensure_ascii=False)
    
    print(f"\nResultados combinados guardados en: {combined_path}")
    return resultados_combinados


def main():
    """Función principal que ejecuta todos los experimentos."""
    print("="*80)
    print("ANÁLISIS COMPARATIVO DE ALGORITMOS PARA EL PROBLEMA DE LAS N-REINAS")
    print("="*80)
    
    try:
        # Ejecutar experimentos
        print("\n[1/3] Ejecutando Experimento 1: Escalabilidad...")
        experimento1_escalabilidad()
        
        print("\n[2/3] Ejecutando Experimento 2: Consistencia...")
        experimento2_consistencia()
        
        print("\n[3/3] Ejecutando Experimento 3: Optimización...")
        experimento3_optimizacion()
        
        # Combinar resultados
        print("\n[4/4] Combinando resultados...")
        combinar_resultados()
        
        print("\n" + "="*80)
        print("TODOS LOS EXPERIMENTOS COMPLETADOS EXITOSAMENTE")
        print("="*80)
        print("\nPróximos pasos:")
        print("1. Ejecutar scripts de generación de gráficos y tablas")
        print("2. Revisar resultados en: experimentos/resultados_brutos/")
        print("3. Ver gráficos en: resultados/graficas/")
        print("4. Ver tablas en: resultados/tablas/")
        
    except KeyboardInterrupt:
        print("\n\nExperimentos interrumpidos por el usuario.")
        combinar_resultados()
    except Exception as e:
        print(f"\n\nError durante la ejecución: {e}")
        import traceback
        traceback.print_exc()
        combinar_resultados()


if __name__ == "__main__":
    main()

