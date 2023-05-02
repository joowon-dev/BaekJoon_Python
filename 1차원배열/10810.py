M,N = map(int, input().split())
k=[0]*M
for i in range(N):
    a,b,c = map(int, input().split())
    for j in range (a-1,b):
        k[j]=c

print(*k)