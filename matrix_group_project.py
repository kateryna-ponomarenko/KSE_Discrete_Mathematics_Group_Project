import random

v = int(random.randint(50,90))
matrix = [[0 for _ in range(v) ] for _ in range(v)]

Hh = int(input("Enter the % of graf: "))
H = v**2 / 100 * Hh

Ah = []
t = True
while H > v**2 - v:
    print("It is too big %. Try again: ")
    Hh = int(input("Enter the % of graf: "))
    H = v ** 2 / 100 * Hh
else:
    while len(Ah) < H:
        u = random.randint(0, v - 1)
        n = random.randint(0, v - 1)
        if u == n:
            continue
        else:
            matrix[u][n] = 1
            matrix[n][u] = 1
            Ah.append((u, n))

V = [x for x in range(1, v+1)]

for i in range(v):
    matrix[i][i] = 0

rows = []
cols = []

nums0 = [" ", 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums1 = [" ", 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
num0 = []
num1 = []
for i in nums1:
    for t in range(10):
        if len(num1) == v + 1:
            break
        num1.append(i)

for i in nums0:
    for t in range(100):
        if len(num0) == v + 1:
            break
        num0.append(i)

num2 = [*nums2 * 10]
num2 = num2[:v]

print("    ", *num0)
print("    ", *num1)
print("      ", *num2)
print("     ", "--" * len(V))
s = 0
a = " "
for row in matrix:
    s += 1
    if s <= 9:
        a = "  "
    elif s <= 99:
        a = " "
    else:
        a = ""
    print(a, s, "|", *row)

t = 0
for row in matrix:
    t += 1
    c = 0
    for i in row:
        c += 1
        if i == 1 and t != c:
            rows.append(t)
            cols.append(c)

ab = []
for i in range(len(rows)):
    ab.append((rows[i], cols[i]))
print(ab)

with open('math.txt', 'w') as f:
    for row in matrix:
        f.write(' '.join(str(x) for x in row) + '\n')
