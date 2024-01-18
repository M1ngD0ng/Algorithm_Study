import sys
from collections import deque

T=int(sys.stdin.readline())
oper=['*','+','-']

def bfs():
  q=deque()
  q.append(([1],1))
  while q: 
    temp,v=q.popleft() 
    if v==N:
      A.append(temp)
    else:
      for o in oper:
        q.append((temp+[o,v+1],v+1))
  

def cal():
  for a in A:
    for i in range(1,len(a)):
      if a[i-1]=='*':
        a[i]=a[i-2]*10+a[i]
        a[i-2]=''
        a[i-1]=''
    ans=0
    op=''
    for i in range(len(a)):
      if a[i]=='':
        continue
      if a[i] in oper:
        op=a[i]
        continue
      if op=='':
        ans+=a[i]
      elif op=='+':
        ans+=a[i]
      elif op=='-':
        ans-=a[i]
    if ans==0:
      for i in range(len(a)):
        if a[i]=='':
          continue
        a[i]=str(a[i])
        if len(a[i])>1:
          sys.stdout.write(a[i][0]+' '+a[i][1])
            
        else:
          sys.stdout.write(str(a[i]))
      print()
  print()

for _ in range(T):
  N=int(sys.stdin.readline())
  A=[]
  bfs()
  cal()
  