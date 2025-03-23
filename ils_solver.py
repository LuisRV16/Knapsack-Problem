import random

# Función para evaluar una solución
def evaluar(solucion, valores, pesos, capacidad):
    valor_total = sum(valores[i] for i in range(len(solucion)) if solucion[i] == 1)
    peso_total = sum(pesos[i] for i in range(len(solucion)) if solucion[i] == 1)
    return valor_total if peso_total <= capacidad else 0  # Penalización si excede la capacidad

# Generar solución inicial aleatoria
def generar_solucion(valores, pesos, capacidad):
    num_objetos = len(valores)
    while True:
        solucion = [random.choice([0, 1]) for _ in range(num_objetos)]
        if sum(pesos[i] for i in range(num_objetos) if solucion[i] == 1) <= capacidad:
            return solucion

# Búsqueda local: intercambio de elementos
def busqueda_local(solucion, valores, pesos, capacidad):
    mejor_sol = solucion[:]
    mejor_valor = evaluar(mejor_sol, valores, pesos, capacidad)

    for i in range(len(solucion)):
        nueva_sol = solucion[:]
        nueva_sol[i] = 1 - nueva_sol[i]  # Intercambia 0 ↔ 1
        
        if sum(pesos[j] for j in range(len(solucion)) if nueva_sol[j] == 1) <= capacidad:
            nuevo_valor = evaluar(nueva_sol, valores, pesos, capacidad)
            if nuevo_valor > mejor_valor:
                mejor_sol, mejor_valor = nueva_sol, nuevo_valor

    return mejor_sol

# Perturbación: cambiar aleatoriamente algunos elementos
def perturbar(solucion, valores, pesos, capacidad, intensidad=2):
    nueva_sol = solucion[:]
    indices = random.sample(range(len(solucion)), min(intensidad, len(solucion)))  # Selecciona algunos índices aleatorios

    for i in indices:
        nueva_sol[i] = 1 - nueva_sol[i]  # Intercambia 0 ↔ 1

    # Asegurar que la nueva solución sea válida
    if sum(pesos[i] for i in range(len(solucion)) if nueva_sol[i] == 1) > capacidad:
        return solucion  # Si la nueva solución no es válida, regresamos la original
    
    return nueva_sol

# Iterated Local Search (ILS)
def iterated_local_search(valores, pesos, capacidad, iteraciones=100):
    solucion_actual = generar_solucion(valores, pesos, capacidad)
    solucion_actual = busqueda_local(solucion_actual, valores, pesos, capacidad)
    mejor_sol = solucion_actual
    mejor_valor = evaluar(mejor_sol, valores, pesos, capacidad)

    for _ in range(iteraciones):
        solucion_perturbada = perturbar(solucion_actual, valores, pesos, capacidad)
        solucion_mejorada = busqueda_local(solucion_perturbada, valores, pesos, capacidad)

        if evaluar(solucion_mejorada, valores, pesos, capacidad) > mejor_valor:
            mejor_sol, mejor_valor = solucion_mejorada, evaluar(solucion_mejorada, valores, pesos, capacidad)

        solucion_actual = solucion_mejorada

    return mejor_sol, mejor_valor

# mejor_solucion, mejor_valor = iterated_local_search(valores, pesos, capacidad, iteraciones=100)
