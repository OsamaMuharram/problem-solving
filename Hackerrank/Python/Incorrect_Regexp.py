import re
n=int(input())
x=[]
for i in range(n):
    x.append(input())
for i in x:
    try:
        re.compile(i)
        is_valid = True
    except re.error:
        is_valid = False
    print(is_valid)
