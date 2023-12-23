import sys
N,M=map(int,sys.stdin.readline().split())

A=set([ sys.stdin.readline().rstrip() for _ in range(N)])


for _ in range(M):
  B=list(sys.stdin.readline().rstrip().split(',')) 
  for s in B:
    if s in A:
      A.remove(s) 
  print(len(A))