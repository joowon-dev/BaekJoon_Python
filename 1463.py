N = int(input())
count=0
arr =[]
arrtemp=[N]
while(1 not in arrtemp):
    arr=[]
    arr=arrtemp[:]
    arrtemp=[]
    for i in arr:
        if(i%3==0):
            arrtemp.append(i/3)
        if(i%2==0):
            arrtemp.append(i/2)
        arrtemp.append(i-1)
    count+=1
print(count)