a = int(input())  # 3
m = []  # [[0, 1, 2,], [1, 5, 3], [2, 3, 4]]
flag = 'Yes'

for i in range(a):
    m.append(list(map(int, input().split())))

for ln in range(a):
    for cl in range(a):
        if m[ln][cl] != m[cl][ln]:
            flag = 'No'
print(flag)
