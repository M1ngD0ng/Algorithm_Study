import sys
import heapq

T=int(sys.stdin.readline())
for _ in range(T):
  M=int(sys.stdin.readline())
  N=0
  if M%10!=0:
    N=M//10+1
  else:
    N=M//10
  A=[]
  for _ in range(N):
    temp=list(map(int,sys.stdin.readline().split()))
    for t in temp:
      A.append(t)
  left=[]
  right=[]
  ans=[]

  for i in range(M):
    if i%2==0:
      heapq.heappush(left,-A[i])
    else:
      heapq.heappush(right,A[i])

    if left and right and -left[0]>right[0]:
      heapq.heappush(left, -heapq.heappop(right))
      heapq.heappush(right, -heapq.heappop(left))

    if i%2==0:
      ans.append(-left[0])

  if M%2==0:
    print(M//2)
    for i in range(M//2):
      if (i+1)%10==0:
        print()
      sys.stdout.write(str(ans[i])+' ')
  else:
    print(M//2+1)
    for i in range(M//2+1):
      sys.stdout.write(str(ans[i])+' ')
      if (i+1)%10==0:
        print()
  print()