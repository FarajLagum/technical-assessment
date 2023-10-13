def calculate_path_cost(path, distance_matrix):
    distance = 0
    for i in range(len(path) - 1):
        start_vertex = path[i] - 1
        end_vertex = path[i + 1] - 1
        distance += distance_matrix[start_vertex][end_vertex]
    return distance


def get_shortest_path(distance_matrix, start_path, unvisited_vertices):
    # print(remaining_vertices)
    if len(unvisited_vertices) == 0:
        return start_path, calculate_path_cost(start_path, distance_matrix)

    shortest_path = None
    shortest_distance = float('inf')

    for i in range(0, len(unvisited_vertices), 2):
        # print(i)
        for vertex in (unvisited_vertices[i], unvisited_vertices[i + 1]):
            # print(remaining_vertices[i])
            current_start_path = start_path + [vertex]
            current_unvisited_vertices = unvisited_vertices[:i] + \
                unvisited_vertices[i + 2:]
            # print(new_remaining)
            path, distance = get_shortest_path(
                distance_matrix, current_start_path, current_unvisited_vertices)
            if distance < shortest_distance:
                shortest_distance = distance
                shortest_path = path

    return shortest_path, shortest_distance


if __name__ == "__main__":

    # Sample input
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

    distanceMatrix_02 = [[0, 1, 2.1, 2.2],
                         [1, 0, 0.9, 3.1],
                         [2.1, 0.9, 0, 1.1],
                         [2.2, 3.1, 1.1, 0]]

    distanceMatrix_03 = [[0.0, 8.1, 9.2, 7.7],
                         [8.1, 0.0, 12.0, 0.9],
                         [9.2, 12.0, 0.0, 11.2],
                         [7.7, 0.9, 11.2, 0.0]]

    distanceMatrix_04 = [[0.0, 8.1, 9.2, 7.7, 9.3, 2.3],
                         [8.1, 0.0, 12.0, 0.9, 12.0, 9.5],
                         [9.2, 12.0, 0.0, 11.2, 0.7, 11.1],
                         [7.7, 0.9, 11.2, 0.0, 11.2, 9.2],
                         [9.3, 12.0, 0.7, 11.2, 0.0, 11.2],
                         [2.3, 9.5, 11.1, 9.2, 11.2, 0.0]]

    distanceMatrix_05 = [[0.0, 0.1, 9.2, 7.7, 9.3, 2.3, 5.1, 10.2, 6.1, 7.0],
                         [0.1, 0.0, 0.1, 0.9, 12.0, 9.5, 10.1, 12.8, 2.0, 1.0],
                         [9.2, 0.01, 0.0, 11.2, 0.7, 11.1, 8.1, 1.1, 10.5, 11.5],
                         [7.7, 0.9, 11.2, 0.0, 11.2, 9.2, 9.5, 12.0, 1.6, 1.1],
                         [9.3, 12.0, 0.7, 11.2, 0.0, 11.2, 8.5, 1.0, 10.6, 11.6],
                         [2.3, 9.5, 11.1, 9.2, 11.2, 0.0, 5.6, 12.1, 7.7, 8.5],
                         [5.1, 10.1, 8.1, 9.5, 8.5, 5.6, 0.0, 9.1, 8.3, 9.3],
                         [10.2, 12.8, 1.1, 12.0, 1.0, 12.1, 9.1, 0.0, 11.4, 12.4],
                         [6.1, 2.0, 10.5, 1.6, 10.6, 7.7, 8.3, 11.4, 0.0, 1.1],
                         [7.0, 1.0, 11.5, 1.1, 11.6, 8.5, 9.3, 12.4, 1.1, 0.0]]

    distanceMatrix_06 = [[0, 	    10, 	15, 	20],
                         [10, 	0, 	    35, 	25],
                         [15, 	35, 	0, 	    30],
                         [20, 	25, 	30, 	0]]

    num_vertices = len(distanceMatrix)
    vertices = list(range(1, num_vertices + 1))
    start_path = []
    start_remaining = vertices

    shortest_path, shortest_distance = get_shortest_path(
        distanceMatrix, start_path, start_remaining)

    print("Shortest Path:", shortest_path)
    print("Shortest Distance:", shortest_distance)
    # print(start_remaining)
