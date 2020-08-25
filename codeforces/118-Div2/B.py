x=int(input())
y=x
z='0'
for i in range(x+1):
    print('  ' * x + z +z.replace(z[-1],'')[::-1])
    x -= 1
    z=z+' '+str(i+1)
if z[-3:] == ' 10':
    z = z.replace(z[-4:], '')
else:
    z = z.replace(z[-3:], '')

for i in range(y+1):
    z = z.replace(z[-1], '')
    z=' '.join(z)
    if z == '':
        break
    print('  ' * (i+1) + z +z.replace(z[-1],'')[::-1])
    z = z.replace(' ', '')
