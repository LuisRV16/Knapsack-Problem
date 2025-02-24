# Solución del Problema de la Mochila con Recocido Simulado

## Importación de Librerías

```python
import random
import math
```

- **`random`**: Se usa para generar valores aleatorios, como soluciones iniciales y vecinos.
- **`math`**: Se usa para cálculos matemáticos, en este caso `math.exp()`, que es clave en el criterio de aceptación de soluciones peores.

---

## Explicación de Funciones y Sintaxis

### 1. Función `compute_value(values, weights, solution)`

```python
def compute_value(values, weights, solution):
    total_value = sum(v * s for v, s in zip(values, solution))
    total_weight = sum(w * s for w, s in zip(weights, solution))
    return total_value, total_weight
```

#### **Uso de `zip()`**

La función `zip()` combina múltiples listas en tuplas de elementos correspondientes. Ejemplo:

```python
valores = [10, 20, 30]
pesos = [1, 3, 5]
solucion = [1, 0, 1]

for v, s in zip(valores, solucion):
    print(v, s)
```

**Salida:**
```
10 1
20 0
30 1
```

Esto permite recorrer las listas al mismo tiempo.

#### **Uso de `sum()` con `zip()`**

```python
total_value = sum(v * s for v, s in zip(values, solution))
```
- Multiplica cada valor por `1` o `0` según la solución.
- Luego, `sum()` acumula los valores seleccionados.

Ejemplo detallado:
```python
values = [10, 20, 30]
solution = [1, 0, 1]
result = sum([10*1, 20*0, 30*1])  # 10 + 0 + 30 = 40
```

---

### 2. Función `get_neighbor(solution)`

```python
def get_neighbor(solution):
    neighbor = solution[:]  # Copia la solución actual
    index = random.randint(0, len(solution) - 1)  # Índice aleatorio
    neighbor[index] = 1 - neighbor[index]  # Alterna entre 0 y 1
    return neighbor
```

#### **Copiar listas con `[:]`**
```python
lista1 = [1, 2, 3]
lista2 = lista1[:]  # Copia lista1 en lista2
```
Esto evita modificar la lista original.

#### **Uso de `random.randint(a, b)`**
```python
numero = random.randint(1, 10)  # Número entre 1 y 10
```

#### **Explicación de `neighbor[index] = 1 - neighbor[index]`**

Si `neighbor[index]` es `1`, se convierte en `0`.
Si es `0`, se convierte en `1`.

Ejemplo:
```python
valor = 1
valor = 1 - valor  # Resultado: 0
```

---

### 3. Función `solve(values, weights, capacity)`

```python
def solve(values, weights, capacity):
    n = len(values)
    current_solution = [random.choice([0, 1]) for _ in range(n)]
    best_solution = current_solution[:]
    best_value, _ = compute_value(values, weights, best_solution)
    
    T = 1000.0  # Temperatura inicial
    cooling_rate = 0.995  # Factor de enfriamiento
    min_T = 1e-3  # Temperatura mínima
```

#### **Uso de Comprensión de Listas**
```python
current_solution = [random.choice([0, 1]) for _ in range(n)]
```
Esto es equivalente a:
```python
current_solution = []
for i in range(n):
    current_solution.append(random.choice([0, 1]))
```

Genera una lista de `n` elementos con valores `0` o `1` al azar.

#### **Uso de `_, current_weight = compute_value(values, weights, current_solution)`**

El guion bajo (`_`) se usa para ignorar valores innecesarios:
```python
a, _ = (5, 10)  # Solo guarda el primer valor (5)
```

#### **Uso de `T *= cooling_rate`**
```python
T = 1000
cooling_rate = 0.995
T *= cooling_rate  # Equivalente a T = T * cooling_rate
```
Esto reduce la temperatura en cada iteración.

---

## Algoritmo de Recocido Simulado

```python
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
```

- Se genera un **vecino** (`get_neighbor()`).
- Se calcula su **valor y peso** (`compute_value()`).
- **Si no excede la capacidad:**
  - Se **actualiza** si es mejor.
  - Si no, se **acepta con cierta probabilidad** basada en la temperatura.
- La **temperatura se reduce** (`T *= cooling_rate`).

Finalmente, se retorna la mejor solución encontrada:
```python
    return best_solution
```

---

## Conclusión
Este código usa **Recocido Simulado** para resolver el problema de la mochila. Explora soluciones cercanas y permite aceptar soluciones subóptimas temporalmente para evitar quedarse atrapado en un mínimo local. 🚀



### Código Super comentado:
```python
import random
import math

def compute_value(values, weights, solution):
    total_value = sum(v * s for v, s in zip(values, solution)) # Multiplica cada uno de los valores por cada uno de los elementos de la solución
    total_weight = sum(w * s for w, s in zip(weights, solution)) # Multiplica cada uno de los pesos por cada uno de los elementos de la solución
    # De esta forma obtiene el valort total de la solución y el peso total de la solución
    return total_value, total_weight # Regresa el valor total y el peso total de la solución

def get_neighbor(solution):
    neighbor = solution[:] # Copia la solución actual
    index = random.randint(0, len(solution) - 1) # Genera un numero aleatorio dentro del rango de indices posibles
    neighbor[index] = 1 - neighbor[index]  # Si el valor es 1, lo cambia a 0 y viceversa
    return neighbor # Retorna la variante de la solución

def solve(values, weights, capacity):
    n = len(values)
    current_solution = [random.choice([0, 1]) for _ in range(n)] # Genera una solución aleatoria
    best_solution = current_solution[:] # Copia la solución actual y esta se asigna como mejor solución
    best_value, _ = compute_value(values, weights, best_solution) # Se obtiene el valor total de la mejor solución hasta el momento
    
    T = 1000.0  # Temperatura inicial
    cooling_rate = 0.995  # Factor de enfriamiento
    min_T = 1e-3  # Temperatura mínima

    """"El recocido simulado basa sus evaluaciones ciclicas en
        simular como se enfría "el codigo" o la ejecución de este
        (de la misma forma en que se enfría un material con el paso del tiempo),
        hasta que llega a su temperatura mínima, en este caso 1e-3.
        En cada ciclo se evalua si la nueva solución es mejor que la anterior."""

    
    while T > min_T:
        new_solution = get_neighbor(current_solution) # Se obtiene la nueva solución
        new_value, new_weight = compute_value(values, weights, new_solution) # Se obtiene el nuevo valor total y el nuevo peso total de esta solución
        _, current_weight = compute_value(values, weights, current_solution) # Se obtiene solamente el peso total de la mejor solución actual, aunque no se usa
        
        """Si el peso total de la nueva solución es
            menor o igual a la capacidad maxima de la mochila
            (Si es un valor válido)"""
        if new_weight <= capacity:
            if new_value > best_value: # Entonces se evalua si el valor total de la nueva solución es mayor al mejor valor total de la solución actual
                best_solution = new_solution[:] # Si es cierto, entonces la mejor solución se actualiza
                best_value = new_value # También se actualiza el mejor valor total
                current_solution = new_solution[:] # Y por ultimo, la nueva mejor solució, se convierte en la solución actual
            else: # Si el valor total de la nueva solución no es mejor que el  valor total de la solución actual
                delta = new_value - best_value # Siempre que entre el else, delta será un valor negativo

                """math.exp(delta / T) se utiliza para obtener la probabilidad de aceptar soluciones
                    Si T es alta, la probabilidad de aceptar soluciones malas es mayor.
                    Si T es baja, se vuelve más estricto y solo acepta mejores soluciones."""
                if math.exp(delta / T) > random.random():
                    current_solution = new_solution[:]
        
        T *= cooling_rate  # Se realiza el enfriamiento
    
    return best_solution # Una vez alcanzada la temperatura mínima, la mejor solución es retornada


values = [10, 20, 30, 40, 50]
weights = [1, 2, 3, 4, 5]
capacity = 10

solution = solve(values, weights, capacity);

print(solution) # [0, 1, 1, 0, 1]

```