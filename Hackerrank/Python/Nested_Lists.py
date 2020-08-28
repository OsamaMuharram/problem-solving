x=[]
z=[]
for i  in range(int(input())):
    a=input()
    b=float(input())
    z.append(b)
    x.append([b,a])
x.sort()
z.sort()
a=z.count(z[0])
for i in range(a,a+z.count(z[a])):
    print(x[i][1])

