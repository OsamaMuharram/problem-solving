from collections import Counter,OrderedDict
x,n=input().split()
num=list(input())
num_count=Counter(num)
for chr, count in num_count.most_common():
    break
print(chr,count)
R_1=int(chr)+1
R_2=int(chr)-1
while 1 :
    if int(n)>count:
        R_1 = R_1 + 1
        R_2 = R_2 - 1
        for i in range(int(chr)+1,R_1):
            if str(i) in num:
                a = num.count(str(i))
                if int(n)-count>a:
                    for j in range(a):
                        num[num.index(str(i))] = str(chr)
                        count=count+a


                else:
                    for j in range(int(n)-count):
                        num[num.index(str(i))] = str(chr)
                    break

        break
    
print(num)


