N = int(input())
count=0
for i in range(N):
    word=input()
    temp=0
    arr=[]
    count+=1
    for i in word:
        if(temp!=i):           
            temp=i
            if( temp not in arr):
                arr.append(temp)
            else:
                count-=1
                break
print(count)