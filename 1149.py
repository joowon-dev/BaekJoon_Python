N= int(input())
arr = []
tempR , tempG, tempB =0,0,0
for i in range(N):
    R,G,B = map (int, input().split())
    A1 = min(tempG+R,tempB+R)
    B1 = min(tempR+G,tempB+G)
    C1 = min(tempG+B,tempR+B)
    tempR , tempG, tempB =A1,B1,C1
print(min(tempR,tempG,tempB))