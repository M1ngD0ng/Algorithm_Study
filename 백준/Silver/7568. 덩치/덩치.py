import sys

N=int(sys.stdin.readline())
A=[]
for _ in range(N):
  A.append(list(map(int,sys.stdin.readline().split())))
  
B=[]
for i in range(N):
  cnt=0
  for a in A:
    if a!=A[i]:
      if a[0]>A[i][0] and a[1]>A[i][1]:
        cnt+=1
  sys.stdout.write(str(cnt+1)+' ')
print()