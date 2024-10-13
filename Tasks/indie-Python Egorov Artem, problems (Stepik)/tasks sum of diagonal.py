a = int(input())
n = []
for i in range(a):
    n.append(list(map(int,input().split())))
    # for j in range(a):
    #     pass
    # n.append(n_temp)
s = 0
for i in range(a):
    for j in range(a):
        if i == j:
            s += n[i][j]
print(s)



