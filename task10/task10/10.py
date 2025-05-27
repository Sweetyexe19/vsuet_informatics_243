import numpy as np


def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def move_max_to_top_left(matrix):
    mat = np.array(matrix)

    max_index = np.unravel_index(np.argmax(mat), mat.shape)
    max_row, max_col = max_index

    if max_row != 0:
        mat[[0, max_row]] = mat[[max_row, 0]]

    if max_col != 0:
        mat[:, [0, max_col]] = mat[:, [max_col, 0]]

    return mat


def read_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            matrix.append([int(x) for x in line.split()])
    return matrix

def write_result_to_file(filename, result):
    with open(filename, 'w') as file:
        if isinstance(result, bool):  # если результат — это булево значение (симметричность)
            if result:
                file.write("Матрица является симметричной.\n")
            else:
                file.write("Матрица не является симметричной.\n")
        else:  # если результат — это матрица
            for row in result:
                file.write(' '.join(map(str, row)) + '\n')

def main():
    input_filename = "vvod.txt"  # Укажите путь к вашему файлу
    output_filename = "vivod.txt"  # Укажите путь для вывода
    matrix = read_matrix_from_file(input_filename)

    if is_symmetric(matrix):
        print("Матрица является симметричной.")
    else:
        print("Матрица не является симметричной.")

    result_matrix = move_max_to_top_left(matrix)
    print("Матрица после перемещения максимального элемента в верхний левый угол:")
    print(result_matrix)

    write_result_to_file(output_filename, is_symmetric(matrix))  # Для симметричности
    write_result_to_file(output_filename, result_matrix)  # Для перемещенной матрицы


if __name__ == "__main__":
    main()
