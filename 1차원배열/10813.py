M,N = map(int, input().split())
k=[i for i in range (1,M+1)]
for i in range(N):
    a,b = map(int, input().split())
    k[a-1],k[b-1]=k[b-1],k[a-1]
print(*k)