T = int(input())
for i in range(T):
    k=int(input())
    n=int(input())
    arr=[[0]*(n+1) for _ in range(k+1)]
    arr[0]=[v for v in range(n+1)]
    for x in range(k):
        for y in range(n+1):
            arr[x+1][y]=sum(arr[x][0:y+1])
    print(arr[k][n])