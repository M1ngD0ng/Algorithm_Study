from collections import deque
import sys
input = sys.stdin.readline
dx, dy, dz = [-1,1,0,0,0,0], [0,0,-1,1,0,0], [0,0,0,0,-1,1]
def bfs():
  q = deque()
  q.append([sz, sx, sy])
  visited[sz][sx][sy] = True
  while q:
    z, x, y = q.popleft()
    for i in range(6):
      nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
      if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C and not visited[nz][nx][ny]:
        if m[nz][nx][ny] == '.' or m[nz][nx][ny] == 'E':
          time[nz][nx][ny] = time[z][x][y] + 1
          q.append([nz, nx, ny])
          visited[nz][nx][ny] = True

while True:
  L, R, C = map(int,input().split())
  if L == 0:
    break
  else:
    m = [[] * R for _ in range(L)]
    time = [[[0] * C for _ in range(R)] for _ in range(L)]
    visited = [[[False] * C for _ in range(R)] for _ in range(L)]
    for i in range(L):
      for j in range(R):
        m[i].append(list(map(str,input())))
      input()
    for k in range(L):
      for i in range(R):
        for j in range(C):
          if m[k][i][j] == 'S':
            sz, sx, sy = k, i, j
          elif m[k][i][j] == 'E':
            ez, ex, ey = k, i, j
    bfs()
    if time[ez][ex][ey]:
      print("Escaped in " + str(time[ez][ex][ey]) + " minute(s).")
    else:
      print("Trapped!")