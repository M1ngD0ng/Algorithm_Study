import sys
import heapq

M, N = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]


def dijstra(start):
  q = []
  heapq.heappush(q, (0, start))
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]
  distance = [[1e8] * M for _ in range(N)]
  distance[0][0] = 0
  while q:
    cnt, now = heapq.heappop(q)

    for i in range(4):
      nx = now[0] + dx[i]
      ny = now[1] + dy[i]
      if not (0 <= nx < N and 0 <= ny < M):
        continue
      if cnt + A[nx][ny] < distance[nx][ny]:
        distance[nx][ny] = cnt + A[nx][ny]
        heapq.heappush(q, (cnt + A[nx][ny], (nx, ny)))

  print(distance[N - 1][M - 1])


dijstra((0, 0))
