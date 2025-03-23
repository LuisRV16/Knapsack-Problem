import json
import time
import read_files
from sim_anneal_solver import solve as sa_solve
from sim_anneal_solver_with_ils import solve as sa_solve_ils
from sim_anneal_solver_comparator import solve as sa_solve_comparator
from sim_anneal_solver_comparator_v2 import solve as sa_solve_comparator_v2
from dp_solver_2 import solve as dp_solve
from utils import compute_value

test_cases = read_files.test_cases()
n = 50
nn = 30

results = {}

case = "s000.kp"
capacity, values, weights = test_cases[case]
max_value = -999999999

start_time = time.time()
for i in range(30):

    sa_solution = sa_solve(values, weights, capacity)
    sa_val, _ = compute_value(values, weights, sa_solution)

    if sa_val > max_value:
        max_value = sa_val
end_time = time.time()

results["results_sa"] = max_value
results["time_sa"] = end_time - start_time
max_value = -999999999

start_time = time.time()
for i in range(30):

    sa_solution = sa_solve_ils(values, weights, capacity)
    sa_val, _ = compute_value(values, weights, sa_solution)

    if sa_val > max_value:
        max_value = sa_val
end_time = time.time()

results["results_sa_ils"] = max_value
results["time_sa_ils"] = end_time - start_time
max_value = -999999999

start_time = time.time()
for i in range(30):

    sa_solution = sa_solve_comparator(values, weights, capacity)
    sa_val, _ = compute_value(values, weights, sa_solution)

    if sa_val > max_value:
        max_value = sa_val
end_time = time.time()

results["results_sa_comparator"] = max_value
results["time_sa_comparator"] = end_time - start_time
max_value = -999999999

start_time = time.time()
for i in range(30):

    sa_solution = sa_solve_comparator_v2(values, weights, capacity)
    sa_val, _ = compute_value(values, weights, sa_solution)

    if sa_val > max_value:
        max_value = sa_val
end_time = time.time()

results["results_sa_comparator_v2"] = max_value
results["time_sa_comparator_v2"] = end_time - start_time

start_time = time.time()
capacity, values, weights = test_cases[case]
dp_val = dp_solve(values, weights, capacity)
results["results_dp"] = int(dp_val)
end_time = time.time()

results["time_dp"] = end_time - start_time

# Guardamos todos los resultados en un archivo JSON
with open("results_sa.json", "w") as f:
    json.dump(results, f)

print("Resultados guardados en 'results_sa.json'")