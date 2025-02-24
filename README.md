# Knapsack Problem Solution using Simulated Annealing

## Importing Libraries

```python
import random
import math
```

- **`random`**: Used for generating random values, such as initial solutions and neighbors.
- **`math`**: Used for mathematical calculations, specifically `math.exp()`, which is crucial for the acceptance criteria of worse solutions.

---

## Explanation of Functions and Syntax

### 1. Function `compute_value(values, weights, solution)`

```python
def compute_value(values, weights, solution):
    total_value = sum(v * s for v, s in zip(values, solution))
    total_weight = sum(w * s for w, s in zip(weights, solution))
    return total_value, total_weight
```

#### **Usage of `zip()`**

The `zip()` function combines multiple lists into tuples of corresponding elements. Example:

```python
values = [10, 20, 30]
weights = [1, 3, 5]
solution = [1, 0, 1]

for v, s in zip(values, solution):
    print(v, s)
```

**Output:**
```
10 1
20 0
30 1
```

This allows simultaneous iteration over multiple lists.

#### **Using `sum()` with `zip()`**

```python
total_value = sum(v * s for v, s in zip(values, solution))
```
- Multiplies each value by `1` or `0` based on the solution.
- Then, `sum()` accumulates the selected values.

Detailed example:
```python
values = [10, 20, 30]
solution = [1, 0, 1]
result = sum([10*1, 20*0, 30*1])  # 10 + 0 + 30 = 40
```

---

### 2. Function `get_neighbor(solution)`

```python
def get_neighbor(solution):
    neighbor = solution[:]  # Copies the current solution
    index = random.randint(0, len(solution) - 1)  # Random index
    neighbor[index] = 1 - neighbor[index]  # Flips between 0 and 1
    return neighbor
```

#### **Copying lists with `[:]`**
```python
list1 = [1, 2, 3]
list2 = list1[:]  # Copies list1 into list2
```
This prevents modifying the original list.

#### **Using `random.randint(a, b)`**
```python
number = random.randint(1, 10)  # Number between 1 and 10
```

#### **Explanation of `neighbor[index] = 1 - neighbor[index]`**
This flips the bit at the given index:

```python
neighbor[index] = 1 if neighbor[index] == 0 else 0
```

---

### 3. Function `solve(values, weights, capacity)`

```python
def solve(values, weights, capacity):
    n = len(values)
    current_solution = [random.choice([0, 1]) for _ in range(n)]  # Generates a random solution
    best_solution = current_solution[:]
    best_value, _ = compute_value(values, weights, best_solution)
    
    T = 1000.0  # Initial temperature
    cooling_rate = 0.995  # Cooling factor
    min_T = 1e-3  # Minimum temperature

    while T > min_T:
        neighbor = get_neighbor(current_solution)
        neighbor_value, neighbor_weight = compute_value(values, weights, neighbor)
        _, current_weight = compute_value(values, weights, current_solution)
        
        if neighbor_weight <= capacity:
            if neighbor_value > best_value or math.exp((neighbor_value - best_value) / T) > random.random():
                current_solution = neighbor[:]
                best_solution = neighbor[:]
                best_value = neighbor_value
        
        T *= cooling_rate  # Reduce temperature
    
    return best_solution
```

---

## Fully Commented Code

```python
import random
import math

def compute_value(values, weights, solution):
    total_value = sum(v * s for v, s in zip(values, solution))  # Multiplies each value by solution selection
    total_weight = sum(w * s for w, s in zip(weights, solution))  # Multiplies each weight by solution selection
    return total_value, total_weight  # Returns total value and weight of the solution

def get_neighbor(solution):
    neighbor = solution[:]  # Copies the current solution
    index = random.randint(0, len(solution) - 1)  # Selects a random index
    neighbor[index] = 1 - neighbor[index]  # Flips between 0 and 1
    return neighbor  # Returns the modified solution

def solve(values, weights, capacity):
    n = len(values)
    current_solution = [random.choice([0, 1]) for _ in range(n)]  # Generates a random initial solution
    best_solution = current_solution[:]  # Copies current solution as the best solution
    best_value, _ = compute_value(values, weights, best_solution)  # Computes value of the best solution
    
    T = 1000.0  # Initial temperature
    cooling_rate = 0.995  # Cooling factor
    min_T = 1e-3  # Minimum temperature
    
    while T > min_T:
        new_solution = get_neighbor(current_solution)  # Generates a neighbor solution
        new_value, new_weight = compute_value(values, weights, new_solution)  # Computes new value and weight
        _, current_weight = compute_value(values, weights, current_solution)  # Gets only current weight
        
        if new_weight <= capacity:  # Ensures the new solution is valid
            if new_value > best_value:  # Checks if the new solution is better
                best_solution = new_solution[:]  # Updates best solution
                best_value = new_value  # Updates best value
            else:
                prob = math.exp((new_value - best_value) / T)  # Acceptance probability
                if random.random() < prob:  # Accepts worse solution with some probability
                    best_solution = new_solution[:]
                    best_value = new_value
        
        T *= cooling_rate  # Decreases temperature
    
    return best_solution  # Returns the best solution found

```
