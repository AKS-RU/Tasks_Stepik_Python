a, b = 4, 4
m = []#[['B','B','W','B'], ['B','B','W','B'], ['W','W','B','W'], ['B','B','W','B']]
for i in range(a):
    m.append(list(input()))
flag = 'Yes'

for ln in range(a - 1):
    if flag == 'No':
        break
    for cl in range(b - 1):
        if m[ln][cl] == m[ln][cl + 1] and m[ln][cl] == m[ln][cl + 1] and m[ln][cl] == m[ln + 1][cl] and m[ln][cl] == m[ln + 1][cl + 1]:
            flag = 'No'
print(flag)
