a = int(input())
n = []
for i in range(a):
    n.append(list(map(int,input().split())))
    # for i in range(a):
    #     pass
    # n.append(n_temp)
s = 0
for i in range(a):
    for i in range(a):
        if i == i:
            s += n[i][i]
print(s)



