import sys
from collections import deque
N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))

ans=deque()
ans.append(N)
if N==1:
  print(N)
else:
  for i in range(N-2,-1,-1):
    cnt=0
    if len(ans)<=A[i]:
      ans.append(i+1)
      continue
    for j in range(len(ans)):
      if cnt==A[i]:
        ans.insert(j,i+1)
        break
      if ans[j]>(i+1):
        cnt+=1
      
  for i in ans:
    sys.stdout.write(str(i)+' ')
  print()