n=int(input())
x=[int(z) for z in input().split()]
count=0
for i in x :
	if x[x[x[i-1]-1]-1] == i:
		print("YES")
		count=1
		break
 
if count==0:
	print("NO")
