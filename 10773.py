K = int(input())
arr=[]
for i in range(K):
    A=int(input())
    if(A==0):
        del arr[len(arr)-1]
    else:
        arr.append(A)
print(sum(arr))