n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    for j in range(1,i+1):
        if j*j==i:
            s+=i
print(s)