a= int(input())
num = int(input())
allprice=0
for i in range(num):
    b,c= map(int,input().split())
    allprice=allprice+b*c

if (a==allprice):
    print('Yes')

else:
    print('No')