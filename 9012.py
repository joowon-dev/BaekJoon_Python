T = int(input())
for i in range(T):
    X= input()
    count=0
    for i in X:
        if(i=='('):
            count+=1
        elif(i==')'):
            count-=1
        if(count<0):
            break
    if(count==0):
        print("YES")
    else: 
        print("NO")