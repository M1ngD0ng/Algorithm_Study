import sys
from collections import deque

N,M=sys.stdin.readline().split()
N=int(N)
A=set([sys.stdin.readline().rstrip() for _ in range(N)])
d=dict()
d['Y']=1
d['F']=2
d['O']=3 
print(len(A)//d[M])

