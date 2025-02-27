# main.py
import matplotlib.pyplot as plt
import json


def main():

    f = open('results.json')
    res = f.read()

    results = json.loads(res)

    dp_results = []
    sa_results = []

    for result in results:
        l = results[result]
        dp_results.append(l[0])
        sa_results.append(l[1])


    # Crear gráfica comparativa: DP (óptimo) vs SA
    plt.figure(figsize=(10, 6))
    plt.scatter(dp_results, sa_results, alpha=0.5, label='Casos de prueba')
    # Línea de referencia y=x
    min_val, max_val = min(dp_results), max(dp_results)
    plt.plot([min_val, max_val], [min_val, max_val], 'r--', label='y = x (óptimo)')
    plt.xlabel("Valor óptimo obtenido (DP)")
    plt.ylabel("Valor obtenido (SA)")
    plt.title("Comparación de soluciones: Programación Dinámica vs Recocido Simulado en Knapsack 0/1")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()