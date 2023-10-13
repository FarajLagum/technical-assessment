from heuristics import nearest_neighbour_heuristic
from exact_algorithm import get_shortest_path
from brute_force import brute_force_algorithm
import time
from inputs import distanceMatrix as distanceMatrix
# from inputs import distanceMatrix_size_20 as distanceMatrix


def print_results(best_path, best_total_distance, execution_time):
    print("----The best path:", best_path)
    print(f"----The best total distance:", best_total_distance)
    print(f"----Execution time: {1000*execution_time:.6f} ms")


num_vertices = len(distanceMatrix)
vertices = list(range(1, num_vertices + 1))


# Nearest Neighbour Heuristic
print("# Heuristic: Nearest Neighbour:")

start_time = time.time()
best_path, best_total_distance = nearest_neighbour_heuristic(
    distanceMatrix, vertices)
end_time = time.time()
execution_time = end_time - start_time
print_results(best_path, best_total_distance, execution_time)


# Exact Algorithm: Dynamic Programming
print("# Exact Algorithm: Dynamic Programming:")
start_time = time.time()
best_path, best_total_distance = get_shortest_path(
    distanceMatrix, [], vertices)
end_time = time.time()
execution_time = end_time - start_time
print_results(best_path, best_total_distance, execution_time)


# Exhaustion: Brute Force Algorithm
print("# Exhaustion: Brute Force:")
start_time = time.time()
best_path, best_total_distance = brute_force_algorithm(
    distanceMatrix, vertices)
end_time = time.time()
execution_time = end_time - start_time
print_results(best_path, best_total_distance, execution_time)
