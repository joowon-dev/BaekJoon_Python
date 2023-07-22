N = int(input())
sum=0
arr = list(map(int,input().split()))
arr.sort()
for i in range(len(arr)):
    sum+=arr[i]*(len(arr)-i)
print(sum)