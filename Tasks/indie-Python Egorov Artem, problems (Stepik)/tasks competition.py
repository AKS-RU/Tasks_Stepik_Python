n, m = map(int,input().split()) #3, 4
m = [] #[[1, 2, 3, 4], [9, 10, 11, 12], [5, 6, 7, 8]]
for i in range(n):
    m.append(list(map(int,input().split())))
sum_m = 0
line = 0

for ln in range(n):
    if sum(m[ln]) > sum_m:
        sum_m = sum(m[ln])
        line = ln
print(sum_m)
print(line)
