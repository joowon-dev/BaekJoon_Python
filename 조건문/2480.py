A,B,C= map(int,input().split())

if(A==B and A==C and B==C):
    print(10000+A*1000)

elif(A!=B and A!=C and B!=C):
    maxnum=max(A,B,C)
    print(maxnum*100)
else:
    if(A==B):
        print(1000+A*100)
    elif(A==C):
        print(1000+A*100)
    else:
        print(1000+B*100)