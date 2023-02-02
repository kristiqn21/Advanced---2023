n = int(input())

matrix = [[int(el) for el in input().split(', ')] for _ in range(n)]
primary = [matrix[i][i] for i in range(n)]
secondary = [matrix[i][n - i - 1] for i in range(n - 1, -1, -1)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary][::-1])}. Sum: {sum(secondary)}")
