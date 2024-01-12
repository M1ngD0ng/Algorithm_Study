import sys

H,W=map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))
top=A[0]

cnt=0
temp=[]
if W==1:
  print(0)
else:
  for i in range(1,W):
    if A[i]<top:
      if i!=W-1:
        isIn=False
        for j in range(i+1,W):
          if A[j]>=A[i]:
            isIn=True
        if not isIn: # 내 뒤로 나보다 큰 건 없음
          top=A[i]
          if temp:
            for t in temp:
              cnt+=(top-t)
          temp.clear()            
        else:
          temp.append(A[i])
      else:
        temp.append(A[i])
    else:
      if temp:
        for t in temp:
          cnt+=(top-t)
      top=A[i]
      temp.clear() 
  if temp:
    for t in temp:
      if t<A[W-1]:
        cnt+=(A[W-1]-t)

  print(cnt)