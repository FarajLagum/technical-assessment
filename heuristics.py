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

    from inputs import distanceMatrix as distanceMatrix

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
