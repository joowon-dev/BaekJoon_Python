N=int(input())
arr=[1,1,2,3,5,8]
if(N<=3):
    print(arr[N-1],1)
elif(N<=6):
    print(arr[N-1],N-2)
else:
    for i in range(N-6):
        arr.append(arr[4+i]+arr[5+i])
    print(arr[N-1],N-2)