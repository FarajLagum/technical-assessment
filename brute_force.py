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

    from inputs import distanceMatrix as distanceMatrix
    
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
