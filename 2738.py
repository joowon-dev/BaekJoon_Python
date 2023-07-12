N, M = map(int,input().split())
A=[[]*M]*N
B=[[]*M]*N
for i in range(N):
  A[i]=list(map( int,input().split()))

for j in range(N):
  B[j]=list(map( int,input().split()))
for i in range (N):
  for j in range(M):
    print(A[i][j]+B[i][j], end=' ')
  print('')