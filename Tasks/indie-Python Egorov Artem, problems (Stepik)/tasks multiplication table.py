a, b = map(int,input().split())
cnt = 0
for ln in range(1,a+1):
    for cl in range(1, a+1):
        if ln*cl == b:
            cnt +=1
print(cnt)
