n=int(input())
l=list(map(int,input().split()))
a=int(input())
b=max(l)
c=0
for i in range(0,n):
    c=l[i]+a
    if c>=b:
        print('True',end=" ")
    else:
        print('False',end=" ")