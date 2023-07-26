a=input()
if (a.count('0')==2):
    print(20)
elif(a.count('0')==1):
    print(9+sum(list(map(int,a))))
else:
    print(sum(list(map(int,a))))