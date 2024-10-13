m = []

for i in range(5):
    m.append(list(map(int,input().split())))
# for ln in range(len(m)):
#     print(m[ln], end=' ')
#     print()
for ln in range(len(m)):
    for cl in range(5):
        if m[ln][cl] == 1:
            n_ln = ln  # index line for 1
            n_cl = cl  # index column for 1
# print(n_ln, n_cl)
cnt = 0
while n_ln != 2:
    if n_ln < 2:
        m[n_ln][n_cl], m[n_ln + 1][n_cl] = m[n_ln + 1][n_cl], m[n_ln][n_cl]
        n_ln +=1
        cnt+=1
    else:
        m[n_ln][n_cl], m[n_ln - 1][n_cl] = m[n_ln - 1][n_cl], m[n_ln][n_cl]
        n_ln -= 1
        cnt += 1
while n_cl != 2:
    if n_cl < 2:
        m[n_ln][n_cl], m[n_ln][n_cl+1] = m[n_ln][n_cl+1], m[n_ln][n_cl]
        n_cl += 1
        cnt += 1
    else:
        m[n_ln][n_cl], m[n_ln][n_cl - 1] = m[n_ln][n_cl - 1], m[n_ln][n_cl]
        n_cl -= 1
        cnt += 1

# for ln in range(len(m)):
#     print(m[ln], end=' ')
#     print()
print(cnt)