N,M = map(int, input().split())
k=[i for i in range (1,N+1)]
for i in range(M):
    a,b = map(int, input().split())
    k[a-1:b]= list(reversed(k[a-1:b]))      
print(*k)