N=input()
for i in N:
    if(90<ord(i)):
        print(chr(ord(i)-32),end='')
    else:
        print(chr(ord(i)+32),end='')