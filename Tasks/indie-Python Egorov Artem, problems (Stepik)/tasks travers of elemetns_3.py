a, b = map(int,input().split()) # a-line, b-column 3, 4
c = [] # [[5, 9, 2, 6],[6, 2, 4, 3], [1, 2, 8, 7]]

for i in range(a):
    c.append(list(map(int,input().split())))

for ln in range(a):
    for cl in range(b-1, -1, -1):
        print(c[ln][cl], end=' ')
    print()