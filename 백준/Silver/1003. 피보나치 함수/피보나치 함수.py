import sys

T=int(input())
A=[ int(input()) for _ in range(T)] 

dp0=[0]*41
dp1=[0]*41
dp0[0],dp0[1],dp0[2]=1,0,1
dp1[0],dp1[1],dp1[2]=0,1,1 

for i in range(3,41):
  dp0[i] =dp0[i-2] +dp0[i-1] 
  dp1[i]=dp1[i-2]+dp1[i-1]

for i in range(T): 
  sys.stdout.write(str(dp0[A[i]])+' '+str(dp1[A[i]])+'\n')
 