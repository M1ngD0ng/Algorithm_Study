from collections import deque

def solution(maps):
    N=len(maps)
    M=len(maps[0])
    
    def bfs(x1,y1,x2,y2):
        q=deque()
        q.append((x1,y1,0))
        visited=[[False]*M for _ in range(N)]
        visited[x1][y1]=True
        dx,dy=[0,0,-1,1],[1,-1,0,0]
        dist=1e9
    
        while(q):
            vx,vy,time=q.popleft()
            
            if time>=dist: continue
            
            for i in range(4):
                nx=vx+dx[i]
                ny=vy+dy[i]
                
                if not (0<=nx<N and 0<=ny<M): continue
                if visited[nx][ny] or maps[nx][ny]=='X': continue
                
                visited[nx][ny]=True
                if (nx,ny)==(x2,y2):
                    dist=min(dist,time+1)
                else:
                    q.append((nx,ny,time+1))
        return dist
            
            
    sx,sy,ex,ey,lx,ly=0,0,0,0,0,0
    
    
    for i in range(N):
        for j in range(M):
            if(maps[i][j]=='S'):
                sx,sy=i,j
            elif(maps[i][j]=='E'):
                ex,ey=i,j
            elif(maps[i][j]=='L'):
                lx,ly=i,j
                
    answer1=bfs(sx,sy,lx,ly)
    answer2=bfs(lx,ly,ex,ey) 
    if answer1==1e9 or answer2==1e9:
        return -1
                
                

    return answer1+answer2