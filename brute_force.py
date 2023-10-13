from itertools import permutations
# import time


def calculate_path_cost(path, distance_matrix):
    distance = 0
    for i in range(len(path) - 1):
        start_vertex = path[i] - 1
        end_vertex = path[i + 1] - 1
        distance += distance_matrix[start_vertex][end_vertex]
    return distance


def generate_valid_permutations(vertices, exclusion_pairs):
    r = int(len(vertices)/2)
    permus = permutations(vertices, r)
    valid_permutations = []
    for perm in permus:
        # exclude permutation if if all elements in the exclusion pair are found in the permutation
        exclude = False
        for pair in exclusion_pairs:
            if set(pair).issubset(perm):  # all(element in perm for element in pair)
                exclude = True
                break
        if not exclude:
            valid_permutations.append(list(perm))
    return valid_permutations


def generate_exclusion_pairs(vertices):
    num_vertices = len(vertices)
    exclusion_pairs = []
    for i in range(1, num_vertices + 1, 2):
        # print(i, i + 1)
        exclusion_pairs.append((i, i + 1))
    return exclusion_pairs


def brute_force_algorithm(distanceMatrix, vertices):

    best_path = []
    best_total_distance = float('inf')

    exclusion_pairs = generate_exclusion_pairs(vertices)
    valid_path_permutations = generate_valid_permutations(
        vertices, exclusion_pairs)

    for valid_path in valid_path_permutations:
        path_cost = calculate_path_cost(valid_path, distanceMatrix)
        # print(path_cost)
        if path_cost < best_total_distance:
            best_total_distance = path_cost
            best_path = valid_path
    return best_path, best_total_distance


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

    # generate_exclusion_pairs()
    exclusion_pairs = generate_exclusion_pairs(vertices)
    print("exclusion_pairs:", exclusion_pairs)

    valid_permutations_list = generate_valid_permutations(
        vertices, exclusion_pairs)

    # for p in valid_permutations_list:
    #     print(p)
    #     time.sleep(0.5)

    shortest_path, shortest_distance = brute_force_algorithm(
        distanceMatrix, vertices)

    print("The best path:", shortest_path)
    print(f"The best total distance:", shortest_distance)
