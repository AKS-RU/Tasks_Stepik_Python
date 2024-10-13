a = int(input())

b = list(map(int,input().split()))

for i in range(a):
    for j in range(1+i, a):
        if b[j] < b[j-1]:
            for v in range(j, 0, -1):
                if b[v] < b[v-1]:
                    b.insert(v-1, b.pop(v))
print(*b)