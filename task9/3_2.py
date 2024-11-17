import numpy as np


def move_max_to_top_left(matrix):
    mat = np.array(matrix)

    max_index = np.unravel_index(np.argmax(mat), mat.shape)
    max_row, max_col = max_index

    if max_row != 0:
        mat[[0, max_row]] = mat[[max_row, 0]]

    if max_col != 0:
        mat[:, [0, max_col]] = mat[:, [max_col, 0]]

    return mat

matrix = [
    [2, 3, 1],
    [5, 20, 6],
    [7, 8, 9]
]

result_matrix = move_max_to_top_left(matrix)
print(result_matrix)