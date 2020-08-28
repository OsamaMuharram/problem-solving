from collections import*

def merge_the_tools(string, k):
    arr=[string[i:i+k] for i in range(0,len(string),k)]
    for j in arr:
        z=''
        print(z.join(list(Counter(j))))

