import random
import math
import json
from utils import compute_value

def get_neighbor(solution, values, weights, capacity):
    neighbor_weight = capacity + 1
    neighbor = solution[:]
    while neighbor_weight <= capacity:
        neighbor = solution[:]
        index = random.randint(0, len(solution) - 1)
        neighbor[index] = 1 - neighbor[index]  # Alterna entre 0 y 1
        _ , neighbor_weight = compute_value(values, weights, neighbor)

    return neighbor

#################################################################

# Metodo para aplicar una perturbación masiva en los datos (flip de n% de bits de la solución)
def get_perturbed_solution(solution, percentage): 
    n = int(len(solution) * percentage)

    neighbor = solution[:]

    for i in get_indexs(len(solution), n):
        neighbor[i] = 1 - neighbor[i]  # Alterna entre 0 y 1

    return neighbor

def get_indexs(length, n): # Metodo para obtener los distintos indices aleatorios de los bits que se cambiaran
    indexs = set()
    while len(indexs) < n:
        indexs.add(random.randint(0, length - 1))
    return indexs

# Metodo para realizar la búsqueda local voraz con el fin de intentar mejorar la solución sin violar restricciones
def local_search(solution, values, weights, capacity): 
    improved = True
    best_solution = solution[:]
    best_value, _ = compute_value(values, weights, best_solution)
    
    while improved:
        improved = False
        for i in range(len(solution)):
            new_solution = best_solution[:]
            new_solution[i] = 1 - new_solution[i]  # Alternar un bit
            new_value, new_weight = compute_value(values, weights, new_solution)

            if new_weight <= capacity and new_value > best_value:
                best_solution = new_solution[:]
                best_value = new_value
                improved = True
    
    return best_solution
#################################################################

def solve(values, weights, capacity):
    # Recocido simulado con ILS y comparación con la versión sin ILS.
    n = len(values)

    best_weight = capacity + 1
    while best_weight > capacity:
        current_solution = [random.choice([0, 1]) for _ in range(n)]
        best_solution = current_solution[:]
        best_value, best_weight = compute_value(values, weights, best_solution)
    
    T = 1000.0  
    cooling_rate = 0.995  
    min_T = 1e-3  
    max_iterations_per_T = 100
    
    ils_better_count = 0
    wo_ils_better_count = 0

    while T > min_T:
        for _ in range(max_iterations_per_T):
            # Generar soluciones con y sin ILS
            perturbed_solution = get_perturbed_solution(current_solution, 0.25)
            new_solution_ils = local_search(perturbed_solution, values, weights, capacity)
            new_solution_wo_ils = get_neighbor(current_solution, values, weights, capacity)

            # Evaluar ambas soluciones
            value_ils, weight_ils = compute_value(values, weights, new_solution_ils)
            value_wo_ils, weight_wo_ils = compute_value(values, weights, new_solution_wo_ils)

            # Contar qué método obtuvo mejor resultado
            if value_ils >= value_wo_ils:
                ils_better_count += 1
                new_solution = new_solution_ils
                new_value = value_ils
                new_weight = weight_ils
                
            elif value_wo_ils > value_ils:
                wo_ils_better_count += 1
                new_solution = new_solution_wo_ils
                new_value = value_wo_ils
                new_weight = weight_wo_ils

            if new_weight <= capacity:
                if new_value > best_value:
                    best_solution = new_solution[:]
                    best_value = new_value
                    current_solution = new_solution[:]
                else:
                    delta = new_value - compute_value(values, weights, current_solution)[0]
                    if delta > 0 or math.exp(delta / max(1e-10, T)) > random.random():
                        current_solution = new_solution[:]

        T *= cooling_rate  

    # Guardar estadísticas en un JSON
    results = {
        "cantidad de iteraciones en las que se obtuvo mejor valor con ils": ils_better_count,
        "cantidad de iteraciones en las que se obtuvo mejor valor sin ils": wo_ils_better_count
    }
    
    with open("ils_vs_wo_ils_results_v2.json", "w") as json_file:
        json.dump(results, json_file, indent=4)

    return best_solution