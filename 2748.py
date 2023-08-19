n = int(input())
fibo=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
if(n<=17):
    print(fibo[n])
else:
    for i in range(n-17):
        fibo.append(fibo[16+i]+fibo[17+i])
    print(fibo[n])