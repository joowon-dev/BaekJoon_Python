T=['A','B','C','D','E']
for i in range(3):
    N= list(map(int,input().split()))
    print(T[N.count(0)-1])