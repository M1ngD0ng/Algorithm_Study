import sys

S=list(sys.stdin.readline().rstrip())
T=[0]+list(sys.stdin.readline().rstrip())
N=len(T)-1
dp=[] 

if len(S)==1:
  if N==1 and S[0]==T[1]:
    print('FRULA')
  else:
    print(S[0])
  sys.exit(0)
if len(S)<N:
  for i in range(len(S)):
    sys.stdout.write(str(S[i]))
  sys.exit(0)
    

# if S[0]==T[1]:
#   dp.append([S[0],1])
# else:
#   dp.append([S[0],0])
# # N==1일때 예외처리 하삼 


for i in range(len(S)):
  last=0
  if dp:
    last=dp[-1][1]
  if T[last+1]==S[i]:
    dp.append([S[i],last+1])
  else:
    if T[1]==S[i]:
      dp.append([S[i],1])
    else:
      dp.append([S[i],0])
  if dp[-1][1]==N:
    for _ in range(N):
      dp.pop()


if not dp:
  print('FRULA')
else:
  for i in range(len(dp)):
    sys.stdout.write(str(dp[i][0]))
print()