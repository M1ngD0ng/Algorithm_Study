import sys
from collections import deque

N=int(sys.stdin.readline())

graph=[ list(map(int,sys.stdin.readline().split())) for _ in range(N) ]

graph.sort()
for g in graph:
  print(g[0], g[1])