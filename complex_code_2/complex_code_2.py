def calculate_complex_metric(x: int, y: int, z: int) -> float:
    #Calculate a complex metric based on input values x, y, and z.
    #This function involves multiple predicates and has a time complexity of O(N^2).
    # Method 1: Calculate a base value based on input parameters
    base_value = calculate_base_value(x, y, z)

    transformed_value = apply_transformation(base_value)

    # Method 3: Apply adjustments based on additional conditions
    final_metric = apply_adjustments(transformed_value, x, y, z)

    return final_metric

def calculate_base_value(x: int, y: int, z: int) -> float:
    base = 0
    for i in range(x):
        for j in range(y):
            base += (i * j) / (z + 1)  # Intentional bug: Should be (z - 1) instead of (z + 1)
    return base

def apply_transformation(value: float) -> float:
    
    #Apply a transformation to the base value.
    
    # Example transformation: Square root of the base value
    transformed_value = value ** 0.5
    return transformed_value

def apply_adjustments(value: float, x: int, y: int, z: int) -> float:
    
    #Apply adjustments to the transformed value based on additional conditions.
    
    # Example adjustment: If x is negative, subtract y squared from the value
    if x < 0:
        value -= y ** 2

    # Example adjustment: If z is greater than 10, add z squared to the value
    if z > 10:
        value += z ** 2

    return value
