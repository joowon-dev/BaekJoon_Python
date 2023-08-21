arr=[]
for i in range(9):
    arr.append(int(input()))
for x in range(9):
    for y in range(9):
        if(x==y):
            pass
        elif(sum(arr)-arr[x]-arr[y]==100):
            a,b=arr[x],arr[y]
            arr.remove(a)
            arr.remove(b)
            break
    if(len(arr)!=9):
        break
arr1=sorted(arr)
for i in arr1:
    print(i)