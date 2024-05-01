import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jewel = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bag = [int(sys.stdin.readline()) for _ in range(K)]

jewel.sort()
bag.sort()

ans = 0
temp = []

for i in range(K):
  while jewel and jewel[0][0] <= bag[i]:
    heapq.heappush(temp, -jewel[0][1])
    heapq.heappop(jewel)

  if temp:
    ans -= heapq.heappop(temp)

print(ans)
