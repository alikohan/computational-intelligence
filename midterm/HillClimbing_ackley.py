import math
import random

def ackley(x, y):
    term1 = -20 * math.exp(-0.2 * math.sqrt(0.5 * (x**2 + y**2)))
    term2 = - math.exp(0.5 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y)))
    result = term1 + term2 + 20 + math.e
    return result

def generate_neighbor(current_point, step):
    new_x = current_point[0] + random.uniform(-step, step)
    new_y = current_point[1] + random.uniform(-step, step)
    return (new_x, new_y)

def hill_climbing(start_point, step_size, max_iterations):
    current_point = start_point
    for _ in range(max_iterations):
        neighbor = generate_neighbor(current_point, step_size)
        if ackley(*neighbor) < ackley(*current_point):
            current_point = neighbor
    return current_point

# Initial starting point
start_point = (random.uniform(-5, 5), random.uniform(-5, 5))
# start_point = (0, 2) # fixed starting point
step_size = 0.1
max_iterations = 1000

# Perform hill climbing
local_minimum = hill_climbing(start_point, step_size, max_iterations)
print("Local minimum found by hill climbing:", local_minimum)
print("Ackley function value at local minimum:", ackley(*local_minimum))
