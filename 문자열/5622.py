S=input()
time=0
for i in range(len(S)):
    if(ord(S[i])>=65 and ord(S[i])<=67):
        time=time+2
    elif(ord(S[i])>=68 and ord(S[i])<=70):
        time=time+3
    elif(ord(S[i])>=71 and ord(S[i])<=73):
        time=time+4
    elif(ord(S[i])>=74 and ord(S[i])<=76):
        time=time+5
    elif(ord(S[i])>=77 and ord(S[i])<=79):
        time=time+6
    elif(ord(S[i])>=80 and ord(S[i])<=83):
        time=time+7
    elif(ord(S[i])>=84 and ord(S[i])<=86):
        time=time+8
    elif(ord(S[i])>=87 and ord(S[i])<=90):
        time=time+9
print(time+len(S))