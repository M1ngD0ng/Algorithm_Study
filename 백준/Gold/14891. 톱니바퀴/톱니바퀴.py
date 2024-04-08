import sys
A=[[] for _ in range(5)] 
for i in range(1,5):
  A[i]=list(map(int,sys.stdin.readline().rstrip()))

K=int(sys.stdin.readline()) 
def findIndex(x):
  if x>7:
    x-=8
  elif x<0:
    x+=8
  return x

def changeIndex(code,wNum):
  if code==1:
    wheel[wNum]=[findIndex(wheel[wNum][0]-1),findIndex(wheel[wNum][1]-1)]
  else:
    wheel[wNum]=[findIndex(wheel[wNum][0]+1),findIndex(wheel[wNum][1]+1)]
  

def rotateWheel(p,wNum,code): 
  temp=[]
  cur=code
  # 왼쪽 계산
  if p=='L':
    for i in range(wNum,1,-1):
      if A[i][wheel[i][0]]!=A[i-1][wheel[i-1][1]]:
        cur*=-1
        temp.append((i-1,cur))
      else:
        break
    for i in temp:
      changeIndex(i[1],i[0])
  else:
    for i in range(wNum,4):
      if A[i][wheel[i][1]]!=A[i+1][wheel[i+1][0]]:
        cur*=-1
        temp.append((i+1,cur))
      else:
        break
    for i in temp:
      changeIndex(i[1],i[0])


wheel=dict() # wheel[i번째 톱니바퀴]=[왼쪽초록, 오른쪽초록]
for i in range(1,5):
  wheel[i]=[6,2]

for _ in range(K):
  a,b=map(int,sys.stdin.readline().split())
  if a>1:
    rotateWheel('L',a,b)
  if a<4:
    rotateWheel('R',a,b)
  changeIndex(b,a) 
ans=0
for i in range(1,5):
  idx=findIndex(wheel[i][0]+2)
  ans+=(A[i][idx]*(2**(i-1)))

print(ans)