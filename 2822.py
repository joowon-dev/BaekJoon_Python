arr=[]
arr2=[]
for i in range(8):
    arr.append(int(input()))
arr1=sorted(arr)
print(sum(arr1[3:8]))
for i in arr1[3:8]:
    arr2.append(arr.index(i))
for i in sorted(arr2):
    print(i+1, end=' ')