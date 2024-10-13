line, columns = map(int,input().split()) #3
m = [] #[[5, 9, 2, 6], [6, 2, 4, 3], [1, 2, 8, 7]]

for i in range(line):
    m.append(list(map(int,input().split())))


for ln in range(line):
    sum_line = 0
    sum_line += sum(m[ln])
    print(sum_line, end=' ')
print()
for cl in range(columns):
    sum_columns = 0
    for ln in range(line):
        sum_columns += m[ln][cl]
    print(sum_columns, end=' ')

