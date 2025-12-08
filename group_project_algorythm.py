import random
INF = 10**9

def shortest_path(i, j, k):
    if k == 0:
        return matrix[i][j]
    # рекурсивна формула Флойда:
    # d_k(i,j) = min(d_{k-1}(i,j), d_{k-1}(i,k) + d_{k-1}(k,j))
    return min(
        shortest_path(i, j, k-1),
        shortest_path(i, k, k-1) + shortest_path(k, j, k-1)
    )

def print_matrix():
    for row in matrix:
        print(*row)



with open('math.txt', 'r') as file:
    line = file.readline()
    line_without_spaces = line.replace(' ', '').strip()
    v = len(line_without_spaces) - 1

    matrix = [[random.randint(0, 1) for _ in range(v)] for _ in range(v)]

    for i in range(v):
        new_line = file.readline()
        new_line_without_spaces = new_line.replace(' ', '').strip()
        lst = list(new_line_without_spaces)
        for j in range(v):
            matrix[i][j] = lst[j]

    print_matrix()
