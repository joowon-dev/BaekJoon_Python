X= 1000-int(input())
(A,X)=divmod(X,500)
(B,X)=divmod(X,100)
(C,X)=divmod(X,50)
(D,X)=divmod(X,10)
(E,X)=divmod(X,5)
(F,X)=divmod(X,1)
print(A+B+C+D+E+F)