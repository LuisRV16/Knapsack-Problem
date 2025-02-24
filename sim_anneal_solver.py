import random
import math
from utils import compute_value

def get_neighbor(solution):
    neighbor = solution[:]
    index = random.randint(0, len(solution) - 1)
    neighbor[index] = 1 - neighbor[index]  # Alterna entre 0 y 1
    return neighbor

def solve(values, weights, capacity):
    n = len(values)
    current_solution = [random.choice([0, 1]) for _ in range(n)]
    best_solution = current_solution[:]
    best_value, _ = compute_value(values, weights, best_solution)
    
    T = 1000.0  # Temperatura inicial
    cooling_rate = 0.995  # Factor de enfriamiento
    min_T = 1e-3  # Temperatura mínima
    
    while T > min_T:
        new_solution = get_neighbor(current_solution)
        new_value, new_weight = compute_value(values, weights, new_solution)
        _, current_weight = compute_value(values, weights, current_solution)
        
        if new_weight <= capacity:
            if new_value > best_value:
                best_solution = new_solution[:]
                best_value = new_value
                current_solution = new_solution[:]
            else:
                delta = new_value - best_value
                if math.exp(delta / T) > random.random():
                    current_solution = new_solution[:]
        
        T *= cooling_rate  # Enfriamiento
    
    return best_solution
