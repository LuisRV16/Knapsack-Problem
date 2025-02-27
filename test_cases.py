# test_cases.py
import random

def generate_test_cases(seed):
    random.seed(seed)
    test_cases = []
    num_cases = 10
    for _ in range(num_cases):
        # Longitud aleatoria entre 50 y 200
        n = random.randint(50, 200)
        # Genera valores y pesos aleatorios
        values = [random.randint(1, 100) for _ in range(n)]
        weights = [random.randint(1, 50) for _ in range(n)]
        total_weight = sum(weights)
        # Capacidad entre el 30% y el 70% del peso total
        capacity = random.randint(int(total_weight * 0.3), int(total_weight * 0.7))
        test_cases.append({
            'values': values,
            'weights': weights,
            'capacity': capacity
        })
    return test_cases

# Prueba rápida si se ejecuta este módulo directamente
if __name__ == '__main__':
    cases = generate_test_cases(42)
    print(cases[0])
