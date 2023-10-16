from heuristics import nearest_neighbour_heuristic
import time


def calculate_path_cost(path, distance_matrix):
    # print("calculating cost of path: ", path)
    distance = 0
    for i in range(len(path) - 1):
        start_vertex = path[i] - 1
        end_vertex = path[i + 1] - 1
        distance += distance_matrix[start_vertex][end_vertex]
    return distance


def get_shortest_path(distance_matrix, start_path, unvisited_vertices, incumbent_distance):
    # print(start_path)

    if len(unvisited_vertices) == 0:
        return start_path, calculate_path_cost(start_path, distance_matrix)

    shortest_path = None
    # shortest_distance = incumbent_distance  # float('inf')
    # print(len(unvisited_vertices))

    for i in range(0, len(unvisited_vertices), 2):

        for vertex in (unvisited_vertices[i], unvisited_vertices[i + 1]):

            current_start_path = start_path + [vertex]
            current_unvisited_vertices = unvisited_vertices[:i] + \
                unvisited_vertices[i + 2:]

            if calculate_path_cost(current_start_path, distance_matrix) > incumbent_distance:
                # print(current_start_path)
                continue

            path, distance = get_shortest_path(
                distance_matrix, current_start_path, current_unvisited_vertices, incumbent_distance)
            # print(path)

            if distance < incumbent_distance:
                # shortest_distance = distance
                incumbent_distance = distance
                shortest_path = path

    return shortest_path, incumbent_distance


def print_results(best_path, best_total_distance, execution_time):
    print("----The best path:", best_path)
    print(f"----The best total distance:", best_total_distance)
    print(f"----Execution time: {execution_time:.6f} seconds")


if __name__ == "__main__":
    # Sample input
    from generate_symmetric_matrix import generate_symmetric_matrix
    from inputs import distanceMatrix_size_20 as distanceMatrix
    # from inputs import distanceMatrix as distanceMatrix
    #distanceMatrix = generate_symmetric_matrix(30)

    num_vertices = len(distanceMatrix)
    vertices = list(range(1, num_vertices + 1))
    start_path = []

    def hybrid_algorithm(vertices, start_path):
        incumbent_path, incumbent_distance = nearest_neighbour_heuristic(
            distanceMatrix, vertices)

        # print("heuristic shortest Path:", incumbent_path)
        # print("heuristic shortest Distance:", incumbent_distance)

        shortest_path, shortest_distance = get_shortest_path(
            distanceMatrix, start_path, vertices, incumbent_distance)

        if shortest_path is None:
            # print("Noet: The heuristic is the best path!")
            shortest_path = incumbent_path

        return shortest_path, shortest_distance

    start_time = time.time()
    shortest_path, shortest_distance = hybrid_algorithm(vertices, start_path)

    end_time = time.time()
    execution_time = end_time - start_time
    print_results(shortest_path, shortest_distance, execution_time)
