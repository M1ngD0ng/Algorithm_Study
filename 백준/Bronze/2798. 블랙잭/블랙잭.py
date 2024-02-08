import sys
from itertools import combinations

N,M=map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))

B=[]
for co in list(combinations(A,3)):
  B.append(sum(co))

B.sort(reverse=True)
for b in B:
  if b<=M:
    print(b)
    break