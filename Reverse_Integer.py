n=int(input())
rev=0
N=0
if n<0:
    n=-n
    N=1
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if N==1:
    print(-rev)
else:
    print(rev)