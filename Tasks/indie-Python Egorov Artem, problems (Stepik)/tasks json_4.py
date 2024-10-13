import json
with open('Abracadabra__1_.txt') as file_txt:
    txt = file_txt.readlines()
# print(txt)
with open('Alphabet.json') as file_json:
    jsn = json.load(file_json)
# print(jsn)
result = ''
for i in txt:
    for j in i:
        if j.isalpha() and j in jsn:
            result += jsn[j]
        else:
            result+=j
print(result)

