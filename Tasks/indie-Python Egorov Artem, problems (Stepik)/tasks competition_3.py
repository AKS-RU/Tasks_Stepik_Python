a, b = map(int, input().split()) #3, 3
m = [] #[[6, 2, 7], [1, 3, 8], [1, 3, 8]]
for i in range(a):
    m.append(list(map(int, input().split())))

max = 0
win = 0
lst = []

for ln in range(a):
    for cl in range(b):
        if max < m[ln][cl]:
            max = m[ln][cl]
            win = ln
for ln in range(a):
    if m[ln].count(max) > 0:
        lst.append(ln)
if len(lst) > 1:
    sum_m = 0
    for ln in lst:
        if sum_m < sum(m[ln]):
            sum_m = sum(m[ln])
            win = ln
print(win)
