Temp_value=-1
Temp_row, Temp_col=0,0
for i in range(9):
  A=list(map(int,input().split()))
  if(Temp_value<max(A)):
    Temp_value=max(A)
    Temp_row=i+1
    Temp_col=A.index(Temp_value)+1
print(Temp_value)
print(Temp_row, Temp_col)