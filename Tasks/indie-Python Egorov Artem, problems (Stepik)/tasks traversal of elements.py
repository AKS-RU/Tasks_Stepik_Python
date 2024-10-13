a = int(input()) #5
b = [] #[[3, 4, 9, 1, 2], [8, 2, 0, 5, 1], [4, 7, 4, 8, 7], [7, 1, 3, 3, 8], [5, 6, 3, 7, 0]]

for i in range(a):
    b.append(list(map(int,input().split())))

for i in range(a):
    for j in range(a):
        print(b[j][i], end=' ')
    print()