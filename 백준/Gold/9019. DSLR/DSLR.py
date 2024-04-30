from collections import deque
import sys

T = int(sys.stdin.readline())

for _ in range(T):
  A, B = map(int, sys.stdin.readline().split())
  visited = [False] * 10001
  visited[A] = True

  q = deque()
  q.append([A, ''])

  while q:
    n, code = q.popleft()

    if n == B:
      print(code)
      break

    d = n * 2 % 10000
    if not visited[d]:
      visited[d] = True
      q.append([d, code + 'D'])

    s = n - 1
    if n - 1 < 0:
      s = 9999
    if not visited[s]:
      visited[s] = True
      q.append([s, code + 'S'])

    l = n // 1000 + (n % 1000) * 10
    if not visited[l]:
      visited[l] = True
      q.append([l, code + 'L'])

    r = n // 10 + (n % 10) * 1000
    if not visited[r]:
      visited[r] = True
      q.append([r, code + 'R'])
