# dp_solver.py

def solve(values, weights, capacity):
    n = len(values)
    dp = [0] * (capacity + 1)
    # Array para registrar el último ítem agregado en cada capacidad
    choice = [-1] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            if dp[w - weights[i]] + values[i] > dp[w]:
                dp[w] = dp[w - weights[i]] + values[i]
                choice[w] = i

    # Reconstrucción de la solución
    solution = [0] * n
    w = capacity
    while w > 0 and choice[w] != -1:
        i = choice[w]
        # Si el ítem aún no ha sido agregado, lo marcamos
        if solution[i] == 0:
            solution[i] = 1
            w -= weights[i]
        else:
            break  # En caso poco probable de duplicación
    return solution