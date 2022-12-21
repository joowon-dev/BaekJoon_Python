a=int(input())
k=map(int,input().split())
b=int(input())
c=0
print(k)
for i in range (a):
    if(b==k[i]):
        c=c+1

print(c)