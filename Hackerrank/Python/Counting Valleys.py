n=int(input())
s=input()
z=0
x=0
for i in s:
    if i =='D':
        x=x-1
    else:
        x=x+1
        if x==0:
            z=z+1
print(z)

