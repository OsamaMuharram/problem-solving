a=int(input())
a_n=[int(z) for z in input().split()]
b=[]
c=[]
for i in a_n:
	if i >=0:
		b.append(i)
	else:
		c.append(i)
 
print(sum(b)-sum(c))
