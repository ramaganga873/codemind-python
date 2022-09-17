n=int(input())
s=0
a=1
for i in str(n):
    s+=int(i)
    a*=int(i)
if a==s:
    print('Spy Number')
else:
    print('Not Spy Number')