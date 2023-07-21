A ,B= map(int,input().split())
arr=[A]
arr1=[]
count=1
while(1):
    for i in arr:
        if(B>int(i)):
            arr1.append(2*i)
            arr1.append(i*10+1)
    arr=arr1.copy()
    arr1=[]
    count+=1
    if(B in arr):
        print(count)
        break
    if(B<arr[0]):
        print(-1)
        break