sum=0
for i in range(4):
    sum+=int(input())
m,s =divmod(sum,60)
print(m)
print(s)