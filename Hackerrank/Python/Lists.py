N = int(input())
z=[]
for i in range(N):
    fun,*l=input().split()
    l=list(map(int,l))
    if fun=='insert':
        z.insert(int(l[0]),l[1])
    elif fun=='print':
        print(z)  
    elif fun == 'remove':
        z.remove(l[0])
    elif fun=='sort' :
        z.sort()   
    elif fun=='append' :
        z.append(l[0])    
    elif fun =='pop' :
        z.pop()
    elif  fun=='reverse':
        z.reverse()     

