while(1):
    A,B,C =  input().split()
    ans='Junior'
    if(A=='#'and B=='0'and C=='0'):
        break
    if(int(B)>17 or int(C)>=80):
        ans='Senior'
    print(A,ans)