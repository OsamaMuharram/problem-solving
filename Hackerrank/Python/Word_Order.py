from collections import Counter
n=int(input())
x=[]
for i in range(n):
    x.append(input())
z=Counter(x)
print(len(z))
print(*z.values())

