import json
import time
import read_files
from ils_solver import iterated_local_search as ils_solve
from dp_solver_2 import solve as dp_solve

test_cases = read_files.test_cases()
n = 50
nn = 30

results = {}

case = "s000.kp"
capacity, values, weights = test_cases[case]
max_value = -999999999

start_time = time.time()
for i in range(30):

    ils_solution, ils_value = ils_solve(values, weights, capacity)

    if ils_value > max_value:
        max_value = ils_value
        
end_time = time.time()

results["results_ils"] = max_value
results["time_ils"] = end_time - start_time

capacity, values, weights = test_cases[case]
dp_val = dp_solve(values, weights, capacity)
results["results_dp"] = int(dp_val)

# Guardamos todos los resultados en un archivo JSON
with open("results_ils.json", "w") as f:
    json.dump(results, f)

print("Resultados guardados en 'results_ils.json'")
