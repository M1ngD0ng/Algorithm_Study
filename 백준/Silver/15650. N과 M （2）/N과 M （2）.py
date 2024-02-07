import sys

from itertools import combinations

N,M=map(int,input().split())

for comb in list(combinations(range(1,N+1),M)):
  for c in comb:
    sys.stdout.write(str(c)+' ')
  print()