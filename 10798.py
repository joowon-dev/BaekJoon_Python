A=[[]]*5
for i in range(5):
  A[i]=input()
for i in range(15):
  for j in range(5):
    try:
      print(A[j][i], end='')
    except: pass