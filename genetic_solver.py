import random

def solve(values, weights, capacity, population_size=100, generations=500, mutation_rate=0.1):
    num_items = len(values)
    
    def fitness(individual):
        total_weight = sum(individual[i] * weights[i] for i in range(num_items))
        total_value = sum(individual[i] * values[i] for i in range(num_items))
        return total_value if total_weight <= capacity else 0
    
    def generate_individual():
        return [random.randint(0, 1) for _ in range(num_items)]
    
    def mutate(individual):
        if random.random() < mutation_rate:
            idx = random.randint(0, num_items - 1)
            individual[idx] = 1 - individual[idx]
        return individual
    
    def crossover(parent1, parent2):
        point = random.randint(1, num_items - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    
    population = [generate_individual() for _ in range(population_size)]
    
    for _ in range(generations):
        population = sorted(population, key=fitness, reverse=True)
        new_population = population[:population_size // 2]
        
        while len(new_population) < population_size:
            p1, p2 = random.choices(population[:50], k=2)
            child1, child2 = crossover(p1, p2)
            new_population.extend([mutate(child1), mutate(child2)])
        
        population = new_population[:population_size]
    
    best_solution = max(population, key=fitness)
    return best_solution, fitness(best_solution)

# Ejemplo de uso
# values = [60, 100, 120]
# weights = [10, 20, 30]
# capacity = 50
# best, best_value = knapsack_genetic(values, weights, capacity)
# print("Mejor solución:", best)
# print("Valor máximo:", best_value)
