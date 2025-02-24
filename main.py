# main.py
import matplotlib.pyplot as plt
from test_cases import generate_test_cases
from dp_solver import solve as dp_solve
from sin_aneeal_solver import solve as sa_solve
from utils import compute_value


def main():
    seed = 42
    test_cases = generate_test_cases(seed)

    dp_results = []
    sa_results = []

    for case in test_cases:
        values = case['values']
        weights = case['weights']
        capacity = case['capacity']

        # Solución con DP
        dp_solution = dp_solve(values, weights, capacity)
        dp_val, _ = compute_value(values, weights, dp_solution)

        # Solución con SA
        sa_solution = sa_solve(values, weights, capacity)
        sa_val, _ = compute_value(values, weights, sa_solution)

        dp_results.append(dp_val)
        sa_results.append(sa_val)

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