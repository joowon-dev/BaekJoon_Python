A=int(input())
arr=[[]*100]*100
temp=0
for i in range(A):
  B, C=map(int,input().split())
  for i in range(len(arr)):
    X=0
    Y=0
    if (arr[i][0]<B and arr[i][0]+10>B):
      X=20-(B+10-arr[i][0])
    if (arr[i][0]>B and arr[i][0]<B+10):
      X=20-(arr[i][0]+10-B)
    if (arr[i][1]<C and arr[i][1]+10>C):
      Y=20-(C+10-arr[i][1])
    if (arr[i][1]>C and arr[i][1]<C+10):
      Y=20-(arr[i][1]+10-C)
    temp=X*Y+temp
  arr.append([B,C])
print(100*A-temp)