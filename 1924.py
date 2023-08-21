x,y = map(int,input().split())
arr=[31,28,31,30,31,30,31,31,30,31,30,31]
arr1= ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
day=0
for i in range(x-1):
    day+=arr[i]
day+=y
print(arr1[day%7])