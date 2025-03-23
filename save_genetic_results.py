import json
import read_files
import time
from genetic_solver import solve as g_solve
from utils import compute_value

test_cases = read_files.test_cases()
n = 50
nn = 30

results = {}

case = "s000.kp"
max_value = -99999999
start_time = time.time()
for i in range(30):
    capacity, values, weights = test_cases[case]

    g_solution, g_best_value = g_solve(values, weights, capacity)

    if g_best_value > max_value:
        max_value = g_best_value
end_time = time.time()

results["result_g"] = max_value
results["time_g"] = end_time - start_time 

with open("results_g.json", "w") as f:
    json.dump(results, f)

print("Resultados guardados en 'results_g.json'")
