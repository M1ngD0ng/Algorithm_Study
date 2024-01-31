import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())

arr=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

score=0

def bfs(x,y):
  q=deque()
  q.append((x,y))
  visited[x][y]=True
  dx,dy=[0,0,1,-1],[1,-1,0,0]
  temp[2].append((x,y))
  target=arr[x][y]

  visited2=[[False]*N for _ in range(N)]
  visited2[x][y]=True
  rainbow=0
  while q:
    vx,vy=q.popleft()

    for i in range(4):
      nx=vx+dx[i]
      ny=vy+dy[i]

      if not (0<=nx<N and 0<=ny<N):
        continue
      if visited2[nx][ny]:
        continue
      if arr[nx][ny] not in [0,target]: # 검은 블록, 다른 번호
        continue
      if arr[nx][ny]==target:
        visited[nx][ny]=True
      elif arr[nx][ny]==0:
        rainbow+=1
      visited2[nx][ny]=True
      temp[2].append((nx,ny))
      q.append((nx,ny))
  temp[3]+=rainbow

def gravity():
  for k in range(N): # 열 인덱스
    for i in range(N-2,-1,-1):
      if arr[i][k] in [1e8, -1]:
        continue
      for j in range(i+1,N):
        if arr[j][k]==1e8:
          if j==N-1:
            arr[j][k]=arr[i][k]
            arr[i][k]=1e8
            break
          else:
            continue
        else:
          if j-1!=i:
            arr[j-1][k]=arr[i][k]
            arr[i][k]=1e8
          break

def rotate():
  new=[[0]*N for _ in range(N)]

  for r in range(N):
    for c in range(N):
      new[N-1-c][r]=arr[r][c]

  return new




while True:
  cntArr=[1e8,1e8,[],0]
  maxLen=0
  visited=[[False]*N for _ in range(N)]
  for i in range(1,M+1): # 칸 안의 번호
    temp=[]
    for j in range(N):
      for k in range(N):
        if arr[j][k]==i and not visited[j][k]:
          temp=[j,k,[],0]
          bfs(j,k)
          tempLen=len(temp[2])
          if tempLen>1:
            if maxLen<tempLen:
              maxLen=tempLen
              cntArr=temp
            elif maxLen==tempLen:
              if temp[3]<cntArr[3]:
                continue
              elif temp[3]>cntArr[3]:
                cntArr=temp
              else:
                if cntArr[0]>temp[0]:
                  continue
                elif cntArr[0]<temp[0]:
                  cntArr=temp
                else:
                  if cntArr[1]>temp[1]:
                    continue
                  elif cntArr[1]<temp[1]:
                    cntArr=temp
                  
                    

  if maxLen==0:
    print(score)
    break
  for x,y in cntArr[2]:
    arr[x][y]=1e8

  score+=(maxLen*maxLen)
  gravity()
  arr=rotate()
  gravity()