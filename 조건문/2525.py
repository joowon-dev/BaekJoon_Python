A,B = map(int,input().split())
C=int(input())

D=B+C
while(1):
    if(D>=60):
        if(A==23):
            A=0
        else:
            A=A+1
        D=D-60
    else:
        break

print(A,D)