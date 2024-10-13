from string import ascii_uppercase
a = int(input())

print([ascii_uppercase[i]*(i+1) for i in range(a)])