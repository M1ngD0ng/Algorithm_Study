import sys 

N,K=map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))

cnt=[0]*(max(A)+1)

left,right=0,0
ans=0
while right<N:
  if cnt[A[right]]<K:
    cnt[A[right]]+=1
    right+=1
  else:
    cnt[A[left]]-=1
    left+=1
  ans=max(ans,right-left)

print(ans)