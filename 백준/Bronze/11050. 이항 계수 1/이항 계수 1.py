import sys
N,K=map(int,sys.stdin.readline().split())
a1,a2,a3=1,1,1

for i in range(1,N+1):
  a1*=i

for i in range(1,(N-K)+1):
  a2*=i

for i in range(1,K+1):
  a3*=i

print(a1//(a2*a3))