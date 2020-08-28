n,m=input().split()
arr=[int(i) for i in input().split()]
a={int(i) for i in input().split()}
b={int(i) for i in input().split()}
z=0
for i in arr:
    if i in a:
        z+=1
    if i in b:
        z-=1
print(z)        

