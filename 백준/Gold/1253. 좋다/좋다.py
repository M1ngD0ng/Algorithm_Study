import sys  

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
A.sort()

cnt=0
if N<3:
  print(0)
else:
  for i in range(N):
    left,right=0,N-1
    while left<right:
      if left==i:
        left+=1
      if right==i:
        right-=1
      if left==right:
        break
      temp=A[left]+A[right]
      if temp==A[i]:
        cnt+=1
        break
      if temp<A[i]:
        left+=1
      elif temp>A[i]:
        right-=1 
  print(cnt)