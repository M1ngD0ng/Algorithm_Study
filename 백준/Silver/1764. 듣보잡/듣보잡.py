import sys 
N,M=map(int,sys.stdin.readline().split())
A=set([ sys.stdin.readline().rstrip() for _ in range(N)])
B=set([ sys.stdin.readline().rstrip() for _ in range(M)])
C=list(A&B)
C.sort()
print(len(C))
for c in C:
  print(c)