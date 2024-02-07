import sys
from itertools import combinations,permutations, combinations_with_replacement


N,M=map(int,input().split())

A=list(map(int,input().split()))

A.sort()
for comb in list(combinations_with_replacement(A,M)):
  for c in comb:
    sys.stdout.write(str(c)+' ')
  print()