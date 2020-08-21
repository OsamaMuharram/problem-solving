x = input()
a=[]
for s in range(0,len(x)) :
	if x[s]=='Q':
		a.append(s)
sum_A=0
for i in range(0,len(a)):
	for j in range(i,len(a)-1):
		sum_A = sum_A+x[a[i]:a[j+1]].count('A')
print(sum_A)
