a=[int(x) for x in input().split()]
k=a[0]
p=a[1]
count=0
for i in range(1,k+1):
	x=str(i)
	z=x[::-1]
	y=int(x+z)
	count=count+y
print(count%p)	
