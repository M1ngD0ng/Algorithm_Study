import sys
import math

A=int(sys.stdin.readline())
arr=[False,False]+[True]*(A+1)
prime=[]
for i in range(2,A+1):
  if arr[i]:
    prime.append(i)
    for j in range(2*i,A+1,i):
      arr[j]=False

ans=0
left,right=0,0
while True:
  if right==len(prime):
    break

  temp=sum(prime[left:right+1])
  if temp>A:
    left+=1
  elif temp<A:
    right+=1
  else:
    ans+=1
    right+=1


print(ans)