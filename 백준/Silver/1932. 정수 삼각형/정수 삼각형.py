import sys

N=int(sys.stdin.readline())
A=[ list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def inRange(i,j):
  return 0<=i<N and 0<=j<len(A[i])
 
if N==1:
  print(A[0][0])

else:
  for i in range(1,N):
    for j in range(len(A[i])):
      temp=[]
      if inRange(i-1,j-1):
        temp.append(A[i][j]+A[i-1][j-1])
      if inRange(i-1,j):
        temp.append(A[i][j]+A[i-1][j])
      if temp:
        A[i][j]=max(temp)
  print(max(A[N-1]))


