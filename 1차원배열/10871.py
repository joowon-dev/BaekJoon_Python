a,b = map(int, input().split())
k= input().split()

for i in range(a):
    if(int(k[i])<b):
        print(k[i],end=' ')