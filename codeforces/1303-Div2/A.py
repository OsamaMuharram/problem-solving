x=int(input())
Arr=[]
for i in range(0,x):
    Arr.append(int(input()))
 
for j in Arr:
    ind=[]
    z=0
    j1=str(j)
    for s in j1:
        if s =='1':
            ind.append(z)
 
        z = z + 1
    if len(ind)>=1:
        print(ind[-1]-(len(ind)-1))
    else:
        print('0')
