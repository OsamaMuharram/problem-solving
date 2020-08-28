n = int(input())
arr =list(map(int, input().split()))
arr.sort()
print(arr[-arr.count(max(arr))-1])

