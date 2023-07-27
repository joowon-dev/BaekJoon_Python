N = int(input())
i=1
count = 0
while(i<=N):
    if(i<100):
        count+=1
    else:
        A = str(i)
        if((int(A[0])+int(A[2]))/2==int(A[1])):
            count+=1
    i+=1
print(count)