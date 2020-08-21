n=int(input())
m=[]
for i in range(0,n):
	m=m+[[x for x in input().split()]]
if m.count(min(m))==(len(m)/2) and m.count(max(m))==(len(m)/2) :
	print ('YES')
	print(min(m)[0],max(m)[0])
else:
	print('NO')
