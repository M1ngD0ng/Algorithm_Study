import sys 

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))

cnt=[]
if M==1:
  print(max(A[0],N-A[0]))
else:
  A.append(N)
  if A[0]!=0:
    A.insert(0,0) 
  for i in range(1,len(A)):
   cnt.append(A[i]-A[i-1]) 

  maxc=0
  for c in cnt[1:len(cnt)-1]:
    if c>maxc:
      maxc=c

  
  if maxc%2==1:
    b=maxc//2+1
  else:
    b=maxc//2  
  print(max(cnt[0],b,cnt[len(cnt)-1]))