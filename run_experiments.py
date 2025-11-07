"""
Script auxiliar para ejecutar experimentos individuales.
Permite ejecutar cada experimento por separado si se desea.
"""

import sys
from experiments import ExperimentRunner

def main():
    if len(sys.argv) < 2:
        print("Uso: python run_experiments.py <numero_experimento>")
        print("  Experimento 1: Escalabilidad")
        print("  Experimento 2: Consistencia")
        print("  Experimento 3: Optimización")
        print("  Todos: Ejecutar todos los experimentos")
        sys.exit(1)
    
    experiment_num = sys.argv[1].lower()
    runner = ExperimentRunner()
    
    if experiment_num == "1" or experiment_num == "escalabilidad":
        runner.experimento1_escalabilidad()
        runner.save_results_to_json("resultados_experimento1.json")
        runner.save_results_to_csv()
    elif experiment_num == "2" or experiment_num == "consistencia":
        runner.experimento2_consistencia()
        runner.save_results_to_json("resultados_experimento2.json")
        runner.save_results_to_csv()
    elif experiment_num == "3" or experiment_num == "optimizacion":
        runner.experimento3_optimizacion()
        runner.save_results_to_json("resultados_experimento3.json")
        runner.save_results_to_csv()
    elif experiment_num == "todos" or experiment_num == "all":
        runner.experimento1_escalabilidad()
        runner.experimento2_consistencia()
        runner.experimento3_optimizacion()
        runner.save_results_to_json()
        runner.save_results_to_csv()
    else:
        print(f"Experimento '{experiment_num}' no reconocido.")
        sys.exit(1)

if __name__ == "__main__":
    main()

