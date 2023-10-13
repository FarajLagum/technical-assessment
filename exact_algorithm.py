def calculate_path_cost(path, distance_matrix):
    distance = 0
    for i in range(len(path) - 1):
        start_vertex = path[i] - 1
        end_vertex = path[i + 1] - 1
        distance += distance_matrix[start_vertex][end_vertex]
    return distance


def get_shortest_path(distance_matrix, start_path, unvisited_vertices):

    if len(unvisited_vertices) == 0:
        return start_path, calculate_path_cost(start_path, distance_matrix)

    shortest_path = None
    shortest_distance = float('inf')

    for i in range(0, len(unvisited_vertices), 2):

        for vertex in (unvisited_vertices[i], unvisited_vertices[i + 1]):

            current_start_path = start_path + [vertex]
            current_unvisited_vertices = unvisited_vertices[:i] + \
                unvisited_vertices[i + 2:]

            path, distance = get_shortest_path(
                distance_matrix, current_start_path, current_unvisited_vertices)
            if distance < shortest_distance:
                shortest_distance = distance
                shortest_path = path

    return shortest_path, shortest_distance


if __name__ == "__main__":
    # Sample input
    from inputs import distanceMatrix as distanceMatrix

    num_vertices = len(distanceMatrix)
    vertices = list(range(1, num_vertices + 1))
    start_path = []

    shortest_path, shortest_distance = get_shortest_path(
        distanceMatrix, start_path, vertices)

    print("Shortest Path:", shortest_path)
    print("Shortest Distance:", shortest_distance)
