def current_vertex_pair_marking(visited, current_vertex):
    if (current_vertex % 2) == 0:
        # print("Even --> vertix + 1 ==> visited")
        visited[current_vertex + 1] = True
    else:
        # print("Odd --> vertix - 1 ==> visited")
        visited[current_vertex - 1] = True
    return visited


def nearest_neighbour_algorithm(distances, start_vertex):
    if start_vertex < 1:
        raise ValueError(
            "start_vertex index should be greater than or equal to 1")
    num_vertices = len(distances)
    # print(num_vertices)
    visited = [False] * num_vertices
    # print(visited)
    path = []
    total_distance = 0

    current_vertex = start_vertex - 1  # the first index is zero
    path.append(current_vertex)
    visited[current_vertex] = True

    visited = current_vertex_pair_marking(visited, current_vertex)
    # print(visited)

    # Repeat until all cities have been visited
    while len(path) < num_vertices:
        nearest_vertex = None
        nearest_distance = float('inf')

        # Find the nearest unvisited vertex
        for vertex in range(num_vertices):
            if not visited[vertex]:
                distance = distances[current_vertex][vertex]
                if distance < nearest_distance:
                    nearest_vertex = vertex
                    nearest_distance = distance

        # Move to the nearest vertex
        current_vertex = nearest_vertex
        # print("current vertex: ", current_vertex)
        if current_vertex is None:
            break
        path.append(current_vertex)
        # print(current_vertex)
        visited[current_vertex] = True
        visited = current_vertex_pair_marking(visited, current_vertex)
        total_distance += nearest_distance

    # add 1 to the index to match the problem statement
    # the indexing of the vertices starts at 1
    path = [x + 1 for x in path]
    # print(path)

    return path, total_distance


def nearest_neighbour_heuristic(distanceMatrix, vertices):
    best_total_distance = float('inf')
    # best_total_distance = 0
    path = []
    for start_vertex in vertices:
        # print(start_vertex)
        path, total_distance = nearest_neighbour_algorithm(
            distanceMatrix, start_vertex)
        if total_distance < best_total_distance:
            best_total_distance = total_distance
            best_path = path
    return best_path, best_total_distance


if __name__ == '__main__':

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

    # distanceMatrix = [[0, 	    10, 	15, 	20],
    #                   [10, 	    0, 	    30, 	25],
    #                   [15, 	    30, 	0, 	    35],
    #                   [20, 	    25, 	35, 	0]]

    num_vertices = len(distanceMatrix)
    vertices = list(range(1, num_vertices + 1))

    best_path, best_total_distance = nearest_neighbour_heuristic(
        distanceMatrix, vertices)

    print("The best path:", best_path)
    print(f"The best total distance:", best_total_distance)

    print("========================================")
    print("Example: We choose the starting vertix:")
    start_vertex = 1
    best_path, total_distance = nearest_neighbour_algorithm(
        distanceMatrix, start_vertex)

    print("The path:", best_path)
    print(
        f"When start_vertex is {start_vertex}, the total distance:", total_distance)

    # =============================
