n=int(input())
l=list(map(int,input().split()))
se=set(l)
su=0
for i in se:
    if(i%2==0):
        su+=i
        
print(su)
    