n=int(input())
l=list(map(int,input().split()))
s=set(l)
su=0
for i in s:
    if(i%2!=0):
        su+=i
print(su)