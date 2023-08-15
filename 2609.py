temp1=0
tmep2=0
A,B = map(int,input().split())
for i in range(1,min(A,B)+1):
    if(A%i==0 and B%i==0):
        temp1=i
for i in range(1,max(A,B)+1):
    if((min(A,B)*i)%max(A,B)==0):
        temp2=(min(A,B)*i)
        break
print(temp1)
print(temp2)