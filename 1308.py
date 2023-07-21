import datetime
y,m,d=map(int,input().split())
dt1 = datetime.datetime(y,m,d)
y1,m1,d1=map(int,input().split())
dt2 = datetime.datetime(y1,m1,d1)
td = dt2 - dt1
if(dt2>=datetime.datetime(y+1000,m,d)):
    print("gg")
else:
    print("D-{}".format(td.days))