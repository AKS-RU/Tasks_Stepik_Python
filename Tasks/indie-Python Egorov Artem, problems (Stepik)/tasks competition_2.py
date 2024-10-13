a, b = map(int,input().split()) # 3, 3
m = [] # [[3, 1, 2], [1, 3, 4], [3, 3, 3]]
for i in range(a):
    m.append(list(map(int,input().split())))
m_max = 0
line = 0
column = 0

for ln in range(a):
    for cl in range(b):
        if m[ln][cl] > m_max:
            m_max = m[ln][cl]
            line = ln
            column = cl
print(m_max)
print(line, column)
