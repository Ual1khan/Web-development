n = int(input())
x = input()
a1 = x.split()
a = list(map(int, a1))
m = max(a)
for i in range(0, n):
    if max(a) == m:
        a.remove(max(a))
print(max(a))