import sys
from collections import deque

N = int(sys.stdin.readline())
A, B = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
par = [[] for _ in range(N + 1)]
son = [[] for _ in range(N + 1)]

for _ in range(M):
  x, y = map(int, sys.stdin.readline().split())
  son[x].append(y)
  par[y].append(x)

visited = [False] * (N + 1)

maxA = -1


def dfs(start, cnt):
  global maxA
  visited[start] = True
  if start == B:
    maxA = cnt
    return
  for i in son[start]:
    if not visited[i]:
      dfs(i, cnt + 1)

  for i in par[start]:
    if not visited[i]:
      dfs(i, cnt + 1)
  return -1


dfs(A, 0)
print(maxA)
