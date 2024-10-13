a, b = map(int, input().split())
m = []
for i in range(a):
    m.append(list(map(int, input().split())))

max = 0
lst = []

for ln in range(a):
    for cl in range(b):
        if max < m[ln][cl]:
            max = m[ln][cl]

for ln in range(a):
    if m[ln].count(max) > 0:
        lst.append(m[ln])

print(len(lst))
