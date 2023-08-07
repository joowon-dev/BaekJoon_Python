C=int(input())
for i in range(C):
    A=[]
    sum=0
    count=0
    A=list(map(int,input().split()))
    for i in range (1,A[0]+1):
        sum+=A[i]
    for i in range(1,A[0]+1):
        if(sum/A[0]<A[i]):
            count+=1
    print(f"{(count/A[0])*100:.3f}%")