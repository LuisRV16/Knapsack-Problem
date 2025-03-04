import matplotlib.pyplot as plt
import json


def main():

    """
        Abre el archivo JSON donde se guardaron 
        los mejores 5 resultados de las 30 corridas
        respectivamente por cada instancia (5 instancias)
    """
    with open('results_dp.json', 'r') as f:
        results = json.load(f)
    with open('results_sa.json', 'r') as f:
        results_sa = json.load(f)
    with open('results_g.json', 'r') as f:
        results_g = json.load(f)

    dp_results = []
    sa_results = []
    genetic_results = []
    errors = []

    for case in results:
        dp_value = results[case]
        sa_value = results_sa[case]
        genetic_value = results_g[case]

        dp_results.append(dp_value)
        sa_results.append(sa_value)
        genetic_results.append(genetic_value)

        # Calcular el error porcentual promedio para este caso
        if dp_value != 0:  # Para evitar división por cero
            error_percent_sa = abs(sa_value - dp_value) / dp_value * 100
            error_percent_ge = abs(genetic_value - dp_value) / dp_value * 100
            error_percent = (error_percent_sa, error_percent_ge)
            errors.append(error_percent)

    # Imprimir los errores porcentuales promedio
    for error in errors:
        print(f"Error porcentual promedio SA: {error[0]:.2f}%", ',', f"Error porcentual promedio Genético: {error[1]:.2f}%")

    # Crear gráfica comparativa: DP (óptimo) vs SA
    plt.figure(figsize=(10, 6))
    plt.scatter(dp_results, sa_results, alpha=0.5, label='Casos de prueba')

    # Línea de referencia y=x (óptimo)
    min_val, max_val = min(dp_results), max(dp_results)
    plt.plot([min_val, max_val], [min_val, max_val], 'r--', label='y = x (óptimo)')

    plt.xlabel("Valor óptimo obtenido (DP)")
    plt.ylabel("Valor obtenido (SA)")
    plt.title("Comparación de soluciones: Programación Dinámica vs Recocido Simulado en Knapsack 0/1")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Crear gráfica comparativa: DP (óptimo) vs genetic
    plt.figure(figsize=(10, 6))
    plt.scatter(dp_results, genetic_results, alpha=0.5, label='Casos de prueba')

    # Línea de referencia y=x (óptimo)
    min_val, max_val = min(dp_results), max(dp_results)
    plt.plot([min_val, max_val], [min_val, max_val], 'r--', label='y = x (óptimo)')

    plt.xlabel("Valor óptimo obtenido (DP)")
    plt.ylabel("Valor obtenido (Genetic)")
    plt.title("Comparación de soluciones: Programación Dinámica vs Genetico en Knapsack 0/1")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
