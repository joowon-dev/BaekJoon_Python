word = input()
count=0
ans=0
wordupper =word.upper()
compword = set(wordupper)
for i in compword:
    if(wordupper.count(i)>count):
        count=wordupper.count(i)
        ans=i
    elif(wordupper.count(i)==count):
        ans='?'
    else:
        pass
print(ans)