N = int(input())
temp=1
Y=0
count=0
for i in range(N,0,-1):
    temp=temp*i
while(temp>10):
    (temp,Y)=divmod(temp,10)
    if(Y==0):
        count+=1
    else:
        break
print(count)