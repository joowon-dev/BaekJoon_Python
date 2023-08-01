N = int(input())
count=0
while(N>1):
    if(N%3==0 or N%3==1):
        count+=1
        if(N%3==1):
            count+=1
        N=N//3
    elif(N%2==0 or N%2==1):
        count+=1
        if(N%2==1):
            count+=1
        N=N//2
    else:
        N-=1
        count+=1
print(count)