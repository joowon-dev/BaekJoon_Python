N ,K = map(int,input().split())
i=0
count=1
arr=[]
for i in range(N):
    arr.append(i+1)
print("<",end="")
while(len(arr)>=1):
    temp=arr[:]
    for i in temp:
        if(count==K):
            if(len(arr)==1):
                print(i,end="")
            else:
                print(i,end=", ")
            arr.remove(i)
            count=1
        else: 
            count+=1
print(">")