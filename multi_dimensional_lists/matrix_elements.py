def read_matrix_func():
    number_of_rows, number_of_columns = map(int, input().split(', '))
    curr_matrix = []
    for row in range(number_of_rows):
        row_data = list(map(int, input().split(', ')))
        curr_matrix.append(row_data)

    return curr_matrix


matrix = read_matrix_func()
sum_matrix = 0

for i in range(len(matrix)):
    curr_row = matrix[i]
    sum_matrix += sum(curr_row)

print(sum_matrix)
print(matrix)
