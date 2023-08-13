N =int(input())
A = set(map(int,input().split()))
M =int(input())
comp = list(map(int,input().split()))
for i in comp:
    print(1) if i in A else print(0)