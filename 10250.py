T= int(input())
for i in range(T):
    H,W,N = map (int,input().split())
    num,floor=divmod(N,H)
    if(floor==0):
        floor=H
        num-=1
    print(floor*100+num+1)