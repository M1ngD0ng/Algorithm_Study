import sys
H,W,N,M=map(int,sys.stdin.readline().split())

A=(H//(N+1))
B=(W//(M+1))
if H%(N+1)!=0:
  A+=1
if W%(M+1)!=0:
  B+=1
print(A*B)