def read_matrix_func():
    number_of_rows, number_of_columns = map(int, input().split(', '))
    curr_matrix = []
    for row in range(number_of_rows):
        row_data = list(map(int, input().split(' ')))
        curr_matrix.append(row_data)

    return curr_matrix


def sum_columns():
    matrix = read_matrix_func()
    rows = len(matrix)
    columns = len(matrix[0])
    sum_of_col = []

    for i in range(columns):
        col_sum = 0
        for j in range(rows):
            col_sum += matrix[j][i]
        sum_of_col.append(col_sum)

    return sum_of_col


data = sum_columns()
for num in data:
    print(num)
