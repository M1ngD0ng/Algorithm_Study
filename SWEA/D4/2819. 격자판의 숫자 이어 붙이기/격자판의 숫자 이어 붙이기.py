from collections import deque

T = int(input())


def bfs(x, y):
    q = deque()
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    q.append(([str(A[x][y])], 1, x, y))
    while q:
        li, cnt, vx, vy = q.popleft()
        if cnt == 7:
            temp=''.join(li)
            if temp not in ans:
                ans.add(temp)
        else:
            for k in range(4):
                nx = dx[k] + vx
                ny = dy[k] + vy
                if not (0<=nx<4 and 0<=ny<4):
                    continue
                q.append((li+[str(A[nx][ny])],cnt+1,nx,ny))


for test_case in range(1, T + 1):
    A = [[] for _ in range(4)]
    for i in range(4):
        temp = list(map(int, input().split()))
        A[i] = temp
    ans = set()
    for i in range(4):
        for j in range(4):
            bfs(i, j)

    print(f'#{test_case} {len(ans)}')
