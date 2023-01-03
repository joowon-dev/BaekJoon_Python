a=int(input())

for i in range(a):
    score=0
    all=0
    str=input()
    for i in str:
        if(i=="O"):
            score=score+1
        else:
            score=0
        all=all+score
    print(all)
