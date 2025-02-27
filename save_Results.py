import json
import read_files
from sim_anneal_solver import solve as sa_solve
from dp_solver import solve as dp_solve
from utils import compute_value

test_cases = read_files.test_cases()
n = 50

best_solution = {}

for case in test_cases:

    capacity, values, weights = test_cases[case]

    # Solución con DP
    dp_solution = dp_solve(values, weights, capacity)
    dp_val, _ = compute_value(values, weights, dp_solution)

    # Solución con SA
    sa_solution = sa_solve(values, weights, capacity)
    sa_val, _ = compute_value(values, weights, sa_solution)

    best_solution[case] = (dp_val, sa_val)

y = json.dumps(best_solution)

f = open("results.json", "w")
f.write(y)
f.close()

print(y)