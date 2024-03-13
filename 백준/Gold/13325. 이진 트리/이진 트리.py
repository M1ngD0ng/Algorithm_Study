import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
a = deque(list(map(int, input().split())))
tree = {i: {} for i in range(1, 2 ** (n+1))}
dp = [[0, 0] for _ in range(2**(n+1))]  # 최장길이, 합
for i in range(1, 2 ** n):
    tree[i][i*2] = a.popleft()
    tree[i][i*2+1] = a.popleft()

def dfs(x, s):
    if x == n-1:
        maxx = max(tree[s][s*2], tree[s][s*2+1])
        dp[s] = [maxx, 2 * maxx]
        return [maxx, 2*maxx]
    else:
        dp[s][0] = max(tree[s][s*2] + dfs(x+1, s*2)[0],
                       tree[s][s*2+1] + dfs(x+1, s*2+1)[0])
        dp[s][1] = dp[s*2][1] + dp[s*2+1][1] + \
            dp[s][0] - dp[s*2][0] + dp[s][0] - dp[s*2+1][0]
        return dp[s]

print(dfs(0, 1)[1])