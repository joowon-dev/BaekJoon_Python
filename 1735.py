A,B=map(int,input().split())
C,D=map(int,input().split())
X=A*D+C*B
Y=B*D
def GCD(x,y):
    while(y):
        x,y=y,x%y
    return x 
N=GCD(X,Y)
print(X//N,Y//N)