x=input()
y=""
for i in range(0,len(x)) :	
	if x[i] in y:
		pass
	else:
		y=y+x[i]	
 
if len(y)%2 ==0:
	print("CHAT WITH HER!")
else:
	print("IGNORE HIM!")
 
