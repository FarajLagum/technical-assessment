import random
# import numpy as np

# def generate_symmetric_matrix(size):
#     np.random.seed(0)  # a random seed
#     random_matrix = np.random.randint(1, 16, size=(size, size))
#     symmetric_matrix = (random_matrix + random_matrix.T) / 2
#     np.fill_diagonal(symmetric_matrix, 0.0)
#     return symmetric_matrix


random.seed(0)


def generate_symmetric_matrix(size):

    symmetric_matrix = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(i, size):
            if i != j:
                random_value = random.randint(1, size*size)
                symmetric_matrix[i][j] = random_value
                symmetric_matrix[j][i] = random_value

    return symmetric_matrix


if __name__ == "__main__":
    matrix_size = 12
    symmetric_matrix = generate_symmetric_matrix(matrix_size)
    print(list(symmetric_matrix))
