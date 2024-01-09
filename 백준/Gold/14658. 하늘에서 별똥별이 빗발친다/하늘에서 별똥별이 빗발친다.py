import sys
input = sys.stdin.readline
N, M, L, K = map(int, input().split())
pos = [tuple(map(int, input().split())) for _ in range(K)]
ans = 0 

for fx, fy in pos:
    for sx, sy in pos:
        stars = 0
        for px, py in pos: 
            if fx <= px <= fx + L and sy <= py <= sy + L: stars += 1
        ans = max(ans, stars)
print(K - ans)