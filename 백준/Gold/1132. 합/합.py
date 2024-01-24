import sys

N=int(sys.stdin.readline())
A=[ list(sys.stdin.readline().rstrip()) for _ in range(N)]

A.sort(key=lambda x:-len(x))
dp1=[[] for _ in range(10)] # 인덱스는 ord(alphabet)-65
maxL=len(A[0])
initial=set()
for a in A:
  initial.add(a[0])
  for i in range(len(a)):
    dp1[ord(a[i])-65].append(10**(len(a)-i-1))

dp2=[]
for i in range(10):
  dp2.append([chr(i+65),sum(dp1[i])])

dp2.sort(key=lambda x:x[1])

if dp2[0][0] in initial:
  temp1=dp2[0][0]
  temp2=dp2[0][1]

  for i in range(1,10):
    if dp2[i][0] not in initial:
      temp1=dp2[i][0]
      temp2=dp2[i][1]
      dp2.pop(i)
      dp2.insert(0,[temp1,temp2])
      break
  
ans=0
for i in range(10): # 큰것부터 9~를 곱해서 합산
  ans+=(dp2[i][1]*i)
  
print(ans)