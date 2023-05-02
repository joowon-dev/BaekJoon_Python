A,B = map(int,input().split())

if(B<45):
    if(A==0):
        A=23
    else:
        A=A-1
    B=60+B-45
else:
    B=B-45

print(A,B)