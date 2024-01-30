import sys
import re

A=sys.stdin.readline().rstrip()
s=re.compile('(100+1+|01)+')
res=s.fullmatch(A)

if res:
  print('SUBMARINE')
else:
  print('NOISE')