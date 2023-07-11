N=int(input())
for i in range(2*N-1):
    if (N<i):
        for j in range(N-i-1):
            print(' ',end='')
        for j in range(2*i+1):
            print('*',end='')
    else:
        for j in range(N-i-1):
            print(' ',end='')
        for j in range(2*i+1):
            print('*',end='')
    print('')


