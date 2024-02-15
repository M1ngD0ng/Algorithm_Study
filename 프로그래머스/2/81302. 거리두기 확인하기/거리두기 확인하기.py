from collections import deque

def bfs(s,x,y):
    q=deque()
    q.append((x,y,0))
    dx,dy=[0,0,1,-1],[1,-1,0,0]
    
    visited=[[False]*5 for _ in range(5)]
    visited[x][y]=True
    while q: 
        vx,vy,dist=q.popleft()
        
        for k in range(4):
            nx=vx+dx[k]
            ny=vy+dy[k]

            if not (0<=nx<5 and 0<=ny<5):
                continue
            if visited[nx][ny]:
                continue
            temp=abs(dx[k])+abs(dy[k])+dist
            visited[nx][ny]=True
            if temp>2 or s[nx][ny]=='X':
                continue
            if s[nx][ny]=='P':
                return 0
            else:
                q.append((nx,ny,temp))
    return 1

def cal(s):
    isPossible=True
    
    
    for i in range(5):
        for j in range(5):
            if s[i][j]=='P':
                isPossible=bfs(s,i,j)
                if not isPossible:
                    return 0
    return 1
    

def solution(places):
    answer = []
    
    for p in places:
        t=[]
        for sp in p:
            t.append(list(sp)) 
        answer.append(cal(t))
        
    return answer