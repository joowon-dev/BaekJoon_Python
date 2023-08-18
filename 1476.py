E,S,M = map(int,input().split())
E1,S1,M1=0,0,0
count=0
while(E!=E1 or S!=S1 or M!=M1):
    E1+=1
    S1+=1
    M1+=1
    if(E1>15):
        E1=1
    if(S1>28):
        S1=1
    if(M1>19):
        M1=1
    count+=1
print(count)