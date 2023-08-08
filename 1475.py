N =input()
arr=['1' ,'2','3','4','5','6','7','8','9','0']
ans=[]
for i in arr:
    ans.append(N.count(i))
if((ans[5]+ans[8])%2==0):
    ans[5]=(ans[5]+ans[8])/2
else:
    ans[5]=(ans[5]+ans[8])/2+1
ans[8]=0
print(int(max(ans)))