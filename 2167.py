import sys
input = sys.stdin.readline
N,M = map(int,input().split())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))
for i in range(int(input())):
    i,j,x,y = map(int,input().split())
    ans=0
    for p in range(i-1,x):
        for q in range(j-1,y):
            ans+=arr[p][q]
    print(ans)