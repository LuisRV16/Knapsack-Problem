def compute_value(values, weights, solution):
    total_value = sum(v * s for v, s in zip(values, solution))
    total_weight = sum(w * s for w, s in zip(weights, solution))
    return total_value, total_weight