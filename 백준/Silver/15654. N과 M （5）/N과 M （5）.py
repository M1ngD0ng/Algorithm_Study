import sys

from itertools import combinations,permutations

N,M=map(int,input().split())
A=list(map(int,input().split()))

A.sort()
for comb in list(permutations(A,M)):
  for c in comb:
    sys.stdout.write(str(c)+' ')
  print()