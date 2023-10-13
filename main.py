from heuristics import nearest_neighbour_heuristic
from exact_algorithm import get_shortest_path
from brute_force import brute_force_algorithm
import time


distanceMatrix = [[0.0, 8.1, 9.2, 7.7, 9.3, 2.3, 5.1, 10.2, 6.1, 7.0],
                  [8.1, 0.0, 12.0, 0.9, 12.0, 9.5, 10.1, 12.8, 2.0, 1.0],
                  [9.2, 12.0, 0.0, 11.2, 0.7, 11.1, 8.1, 1.1, 10.5, 11.5],
                  [7.7, 0.9, 11.2, 0.0, 11.2, 9.2, 9.5, 12.0, 1.6, 1.1],
                  [9.3, 12.0, 0.7, 11.2, 0.0, 11.2, 8.5, 1.0, 10.6, 11.6],
                  [2.3, 9.5, 11.1, 9.2, 11.2, 0.0, 5.6, 12.1, 7.7, 8.5],
                  [5.1, 10.1, 8.1, 9.5, 8.5, 5.6, 0.0, 9.1, 8.3, 9.3],
                  [10.2, 12.8, 1.1, 12.0, 1.0, 12.1, 9.1, 0.0, 11.4, 12.4],
                  [6.1, 2.0, 10.5, 1.6, 10.6, 7.7, 8.3, 11.4, 0.0, 1.1],
                  [7.0, 1.0, 11.5, 1.1, 11.6, 8.5, 9.3, 12.4, 1.1, 0.0]]


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
