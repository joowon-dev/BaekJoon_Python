N = int(input())
for i in range(N):
    print(" "*(N-i-1),end="")
    print("*"*(1+2*i),end="")
    print("")
for i in range(1,N):
    print(" "*i,end="")
    print("*"*(2*(N-i)-1),end="")
    print("")