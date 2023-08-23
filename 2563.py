A=int(input())
arr=[[0 for i in range(100)] for i in range(100)]
temp=0
for i in range(A):
  B, C=map(int,input().split())
  for x in range(10):
    for y in range(10):
      arr[x+B][y+C]=1
count=0
for x in range(100):
  for y in range(100):
    if (arr[x][y]==1):
      count+=1
print(count)