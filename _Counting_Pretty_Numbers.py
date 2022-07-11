def ispretty(n):
    r=n%10
    if r==2 or r==3 or r==9:
        return 1
    else:
        return 0
        
n=int(input())
for i in range(n):
    c=0
    a,b=map(int,input().split())
    for j in range(a,b+1):
        if ispretty(j):
            c+=1
    print(c)