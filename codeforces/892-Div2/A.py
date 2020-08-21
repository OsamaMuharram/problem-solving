n = int(input())
if 2<=n<=100000:
	a=[int(x) for x in input().split()]
	b=[int(x) for x in input().split()]
	if 0<= max(a) <=10**9and 0<=max(b)<=10**9:
			
		i=max(b)
		b.remove(max(b))
		j=max(b)
		if (i+j)>=sum(a):
			print("YES")
		else:
			print("NO")
