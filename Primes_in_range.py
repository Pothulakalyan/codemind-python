def prime(k):
    if k==1:
        return 0
    for i in range(2,int(k**0.5)+1,1):
        if k%i==0:
            return 0
            break
    return 1
    
x =int(input())
y=int(input())
c=0
for i in range(x,y+1):
    if prime(i):
        c+=1
print(c)

