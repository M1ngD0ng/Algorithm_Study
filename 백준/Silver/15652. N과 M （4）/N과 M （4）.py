import sys

from itertools import combinations,permutations, combinations_with_replacement
N,M=map(int,input().split())
for comb in list(combinations_with_replacement(range(1,N+1),M)):
  for c in comb:
    sys.stdout.write(str(c)+' ')
  print()