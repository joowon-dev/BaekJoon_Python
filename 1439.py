S = input()
arr=[]
temp=4
for i in S:
    if(temp!=i):
        arr.append(i)
        temp=i
    else:
        pass
print(min(arr.count('1'),arr.count('0')))