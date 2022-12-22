a=int(input())
k=input().split()
b=int(input())
c=0
for i in range (a):
    if(b==int(k[i])):
        c=c+1

print(c)