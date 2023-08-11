N = int(input())
for i in range(N):
    print("*"*(1+i),end="")
    print(" "*(2*N-(i*2)-2),end="")
    print("*"*(1+i),end="")
    print("")
for i in range(2,N+1):
    print("*"*(1+(N-i)),end="")
    print(" "*(2*N-((N-i)*2)-2),end="")
    print("*"*(1+(N-i)),end="")
    print("")