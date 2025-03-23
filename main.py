import matplotlib.pyplot as plt
import json

def main():
    case = "s000.kp"

    # Cargar resultados desde archivos JSON
    with open('results_dp.json', 'r') as f:
        results = json.load(f)
    with open('results_sa.json', 'r') as f:
        results_sa = json.load(f)
    with open('results_g.json', 'r') as f:
        results_g = json.load(f)
    with open('results_ils.json', 'r') as f:
        results_ils = json.load(f)

    # Obtener resultados de cada método
    dp_result = results_sa["results_dp"]  # Óptimo (Programación Dinámica)
    sa_result = results_sa["results_sa"]
    ils_result = results_ils["results_ils"]
    sa_result_with_ils = results_sa["results_sa_ils"]
    sa_result_union_ils = results_sa["results_sa_comparator"]
    sa_result_union_ils_v2 = results_sa["results_sa_comparator_v2"]
    genetic_result = results_g["result_g"]

    # Lista de resultados obtenidos
    results = [sa_result, 
               genetic_result,
               ils_result,
               sa_result_with_ils, 
               sa_result_union_ils, 
               sa_result_union_ils_v2]

    labels = ["SA", "Genético", "ILS", "SA+ILS", "SA∪ILS", "SA∪ILS v2"]

    # Calcular los errores porcentuales
    errors = []
    if dp_result != 0:  # Evitar división por cero
        errors = [abs(res - dp_result) / dp_result * 100 for res in results]

    # Imprimir los errores porcentuales
    for label, error in zip(labels, errors):
        print(f"Error porcentual {label}: {error:.2f}%")

    # ----------------------------- #
    # 📊 Gráfica de errores porcentuales
    # ----------------------------- #
    plt.figure(figsize=(10, 5))

    # Puntos de resultados
    plt.scatter(labels, results, color='blue', label="Resultados Metaheurísticos", s=100)
    
    # Línea del óptimo
    plt.axhline(y=dp_result, color='red', linestyle='--', label="Óptimo (DP)")

    # Añadir etiquetas de error a cada punto
    for i, (label, res, error) in enumerate(zip(labels, results, errors)):
        plt.text(i, res, f"{error:.2f}%", fontsize=10, ha='right', va='bottom')

    # Configuración de la gráfica
    plt.xlabel("Métodos")
    plt.ylabel("Valor obtenido")
    plt.title("Comparación de Resultados con el Óptimo")
    plt.legend()
    plt.grid(True)

    # Mostrar la gráfica de errores porcentuales
    plt.show()

    # ----------------------------- #
    # 📊 Gráfica de tiempos de ejecución
    # ----------------------------- #
    
    # Lista de tiempos (corregida)
    times = [results_sa["time_sa"],
             results_g["time_g"],
             results_ils["time_ils"],
             results_sa["time_sa_ils"],
             results_sa["time_sa_comparator"],
             results_sa["time_sa_comparator_v2"]]

    # Crear la gráfica de barras
    plt.figure(figsize=(10, 5))
    plt.bar(labels, times, color=['blue', 'green', 'orange', 'purple', 'brown', 'pink'])

    # Añadir etiquetas de tiempo sobre cada barra
    for i, time in enumerate(times):
        plt.text(i, time, f"{time:.2f}s", ha='center', va='bottom', fontsize=10)

    # Configuración de la gráfica
    plt.xlabel("Métodos")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title("Comparación de Tiempos de Ejecución")
    plt.grid(axis='y')

    # Mostrar la gráfica de tiempos
    plt.show()

# Ejecutar la función principal
main()
