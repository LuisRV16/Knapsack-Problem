import json
import read_files
from sim_anneal_solver import solve as sa_solve
from utils import compute_value

test_cases = read_files.test_cases()
n = 50
nn = 30

results = {}

for case in test_cases:
    max_value = -999999999
    for i in range(30):
        capacity, values, weights = test_cases[case]

        sa_solution = sa_solve(values, weights, capacity)
        sa_val, _ = compute_value(values, weights, sa_solution)

        if sa_val > max_value:
            max_value = sa_val

    results[case] = max_value

# Guardamos todos los resultados en un archivo JSON
with open("results_sa.json", "w") as f:
    json.dump(results, f)

print("Resultados guardados en 'results_sa.json'")
