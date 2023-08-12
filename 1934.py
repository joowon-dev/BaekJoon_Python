T = int(input())
for i in range(T):
    A,B=map(int,input().split())
    for j in range(1,A+1):
        if((B*j)%A==0):
            print(B*j)
            break