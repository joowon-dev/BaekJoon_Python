arr=[]
N=int(input())
for i in range(N):
    arr.append([i+1,0])
count =0
num=1
ans=0
while(1):
    if(arr[count][1]==0):
        num+=1
        if(num==2):
            ans+=1
            num=0
            arr[count][1]=1
            print(arr[count][0],end=' ')
            if(ans==N):
                break
    count+=1
    if (count>=N):
        count=0