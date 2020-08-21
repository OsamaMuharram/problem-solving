list_a=[int(x) for x in input().split()]
n=list_a[0]
m=list_a[1]
s=input()
list_m=[]
for i in range(0,m):
	list_m=list_m+[[x for x in input().split()]]
for i in range(0,m):
	for j in range (0,4):
		l =int(list_m[i][0])
		r =int(list_m[i][1])
		c0=list_m[i][2]
		c1=list_m[i][3]
		s=s[0:l-1]+s[l-1:r].replace(c0,c1)+s[r:len(s)]
print(s)
