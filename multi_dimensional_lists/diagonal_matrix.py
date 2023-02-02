def read_matrix_func():
    number_of_rows = int(input())
    curr_matrix = []

    for row in range(number_of_rows):
        row_data = list(map(int, input().split(' ')))
        curr_matrix.append(row_data)

    return curr_matrix


matrix = read_matrix_func()


def some_diagonal(matrix):
    some_of_diagonal = [matrix[i][i] for i in range(len(matrix))]

    return sum(some_of_diagonal)


print(some_diagonal(matrix))
