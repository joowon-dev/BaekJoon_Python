N= int(input())
A=[]*N
A=list(map(int,input().split()))
B, C = map(int,input().split())
count=0
for i in A:
    if(i-B>0):
        X,Y=divmod(i-B,C)
    else:
        X,Y=0,0
    if(Y ==0):
        count=count+1+X
    else:
        count=count+2+X
print(count)