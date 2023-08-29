arr = [0 for i in range(20000001)]
N = int(input())
n=list(map(int,input().split()))
for i in n:
    arr[i+10000000]+=1
M=int(input())
m=list(map(int,input().split()))
for i in m:
    print(arr[i+10000000],end=' ')