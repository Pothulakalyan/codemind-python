a=int(input())
l=list(map(int,input().split()))
e=o=0
for i in range(0,a):
    if i%2==0:
        e+=l[i]
    else:
        o+=l[i]
if e==o:
    print('YES')
else:
    print('NO')