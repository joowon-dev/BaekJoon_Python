X= int(input())
arr=[64,32,16,8,4,2,1]
sum=0
count=0
for i in arr:
    if(X-sum>=i):
        sum+=i
        count+=1
        if(sum==X):
            break
print(count)