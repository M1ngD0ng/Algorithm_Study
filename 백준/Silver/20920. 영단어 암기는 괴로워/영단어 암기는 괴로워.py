import sys

N,M=map(int,sys.stdin.readline().split())
A={}
for _ in range(N):
  s=sys.stdin.readline().rstrip()
  if len(s)<M:
    continue
  else: # 단어가 M이상인 경우
    if s in A: # 단어가 있는 경우
        A[s] += 1
    else: # 단어가 없는 경우
        A[s] = 1

B=sorted(A.items(), key=lambda x:(-x[1],-len(x[0]),x[0]))
for i in B:
  print(i[0])