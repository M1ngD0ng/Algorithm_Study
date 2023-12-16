N=int(input())
P=list(map(int,input().split()))

P.sort(reverse=True)

ans=0
x=1
for i in P:
  ans=ans+i*x
  x+=1

print(ans)