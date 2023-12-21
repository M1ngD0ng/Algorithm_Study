import sys
T=int(sys.stdin.readline())

for _ in range(T):
  A=list(map(int,sys.stdin.readline().split()))
  N=A[0]
  
  total=0
  
  for i in range(2,len(A)): 
    cnt=0
    for j in range(1,i):
      if A[j]>A[i]:
        cnt+=(i-j)
        A.insert(j,A[i])
        A.pop(i+1)
        break  
    total+=cnt
  sys.stdout.write(str(N)+' '+str(total)+'\n')