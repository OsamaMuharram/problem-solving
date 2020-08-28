#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    x=ar
    x.sort()
    z=0
    y=[]
    for i in range(0,len(x)):
        if z<len(x):
            y.append(x.count(x[z]))
            z=z+x.count(x[z])
        else:
            break
    res = sum(list(map(lambda s:math.floor(s/2),y)))
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

