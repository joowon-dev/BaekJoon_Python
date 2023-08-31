T = int(input())
for i in range(T):
    arr=input().split()
    for j in range(len(arr)):
        print(arr[j][::-1],end=' ')
    print('')