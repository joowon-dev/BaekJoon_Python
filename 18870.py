import sys
N= int(sys.stdin.readline())
X= list(map(int,input().split()))
com=sorted(list(set(X)))
dic = {com[i]:i for i in range(len(com))}
for i in X:
    print(dic[i],end=' ')