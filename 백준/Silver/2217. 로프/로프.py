N=int(input())

A=[int(input()) for _ in range(N)]
A.sort()
ans=[]

cnt=N
for i in range(N):
  ans.append(A[i]*cnt)
  cnt-=1
 
print(max(ans))