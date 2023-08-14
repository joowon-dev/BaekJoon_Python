A,B,N = map(int,input().split())
ans=0
for i in range(N+1):
    ans = A//B
    A=A%B*10
print(ans)