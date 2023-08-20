arr=['c=','c-','dz=','d-','lj','nj','s=','z=']
word=input()
temp=0
for i in arr:
    word=word.replace(i,'a')
print(len(word))