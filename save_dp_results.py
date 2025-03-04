import json
import read_files
from dp_solver_2 import solve as dp_solve

test_cases = read_files.test_cases()
n = 50
nn = 30

results = {}

for case in test_cases:
    capacity, values, weights = test_cases[case]

    dp_val = dp_solve(values, weights, capacity)

    results[case] = int(dp_val)

with open("results_dp.json", "w") as f:
    json.dump(results, f)

print("Resultados guardados en 'results_dp.json'")
