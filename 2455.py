A1,A2 = map(int,input().split())
B1,B2 = map(int,input().split())
C1,C2 = map(int,input().split())
D1,D2 = map(int,input().split())
temp1 = A2
temp2 = A2-B1+B2
temp3 = temp2-C1+C2
temp4= temp3-D1
print(max(temp1,temp2,temp3,temp4))