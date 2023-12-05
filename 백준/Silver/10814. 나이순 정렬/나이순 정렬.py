import sys
from collections import deque

N=int(sys.stdin.readline())

M=[[] for _ in range(N)]
for i in range(N):
  A,B=sys.stdin.readline().split()
  M[i]=[int(A), B, i]

M=sorted(M, key=lambda x:x[0])
for i in range(N):
  print(M[i][0], M[i][1])