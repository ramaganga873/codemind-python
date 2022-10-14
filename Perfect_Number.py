n=int(input())
b=0
for i in range(1,n):
    if n%i==0:
        b+=i
if b==n:
    print(True)
else:
    print(False)
        
    