sum=0
for i in range(5):
    N=0
    N=int(input())
    if(N<40):
        N=40
    sum+=N
print(int(sum/5))