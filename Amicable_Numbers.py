n=int(input())
m=int(input())
t=0
g=0
for i in range(1,n):
    if n%i==0:
        t+=i
for r in range(1,m):
    if m%r==0:
        g+=r
if g==n and t==m:
     print('Amicable')
else:
     print('Not Amicable')
