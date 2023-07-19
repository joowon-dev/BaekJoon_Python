N= int(input())
answer=1
for i in range(1,13):
    answer=answer*i
    if(i==N or N==0):
        print(answer)
        break