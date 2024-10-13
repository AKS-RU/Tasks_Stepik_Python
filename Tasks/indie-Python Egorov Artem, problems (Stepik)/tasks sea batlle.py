line, columns = map(int,input().split()) # 4, 4
m = [] #[['*', '*', '*', '*'], ['*', '*', '.', '.', ], ['*', '.', '.', '.'], ['*', '.', '.', '.']]
cnt = 0
for i in range(line):
    m.append(list(map(str,input())))

for ln in range(line):
    if m[ln].count('*') < columns-1:
        for cl in range(columns):
            if m[ln][cl] == '.':
                a = m[ln][cl]
                if cl == columns-1:
                    if ln == 0 or ln == line-1:
                        if ln == 0:
                            if a == m[ln][cl - 1] and a == m[ln + 1][cl]:
                                cnt += 1
                        else:
                            if a == m[ln][cl - 1] and a == m[ln - 1][cl]:
                                cnt += 1
                    else:
                        if a == m[ln][cl-1] and a == m[ln-1][cl] and a == m[ln+1][cl]:
                            cnt +=1
                elif cl == 0:
                    if ln == 0 or ln == line - 1:
                        if ln == 0:
                            if a == m[ln][cl + 1] and a == m[ln + 1][cl]:
                                cnt += 1
                        else:
                            if a == m[ln][cl + 1] and a == m[ln - 1][cl]:
                                cnt += 1
                    else:
                        if a == m[ln][cl + 1] and a == m[ln - 1][cl] and a == m[ln + 1][cl]:
                            cnt += 1
                elif ln == line-1:
                    if cl == 0 or cl == columns - 1:
                        if cl == 0:
                            if a == m[ln-1][cl] and a == m[ln][cl+1]:
                                cnt += 1
                        else:
                            if a == m[ln][cl - 1] and a == m[ln - 1][cl]:
                                cnt += 1
                    else:
                        if a == m[ln][cl + 1] and a == m[ln - 1][cl] and a == m[ln][cl-1]:
                            cnt += 1
                elif ln == 0:
                    if cl == 0 or cl == columns - 1:
                        if cl == 0:
                            if a == m[ln + 1][cl] and a == m[ln][cl + 1]:
                                cnt += 1
                        else:
                            if a == m[ln][cl - 1] and a == m[ln + 1][cl]:
                                cnt += 1
                    else:
                        if a == m[ln][cl + 1] and a == m[ln + 1][cl] and a == m[ln][cl - 1]:
                            cnt += 1
                else:
                    if m[ln][cl] == m[ln+1][cl] and a == m[ln][cl - 1] and a == m[ln][cl + 1] and a == m[ln-1][cl]:
                        cnt += 1
print(cnt)