a=int(input())
b=list(map(int,input().split()))
c=max(b)
d=0
for i in b:
    d=d+i/c*100
print(d/a)