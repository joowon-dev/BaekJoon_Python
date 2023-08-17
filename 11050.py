N,K = map(int,input().split())
ans=1
temp=1
for i in range(K,0,-1):
    temp=temp*i
for i in range(K):
    ans=ans*N
    N-=1
print(int(ans/temp))