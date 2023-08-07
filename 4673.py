arr=[]
for i in range(10000):
    arr.append(i)
for i in range (10000):
    try:
        arr.remove(i+sum(map(int,str(i))))
    except:
        pass
for i in arr:
    print(i)