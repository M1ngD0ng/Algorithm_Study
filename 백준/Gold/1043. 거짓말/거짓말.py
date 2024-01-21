import sys 

N,M=map(int,sys.stdin.readline().split())
know=list(map(int,sys.stdin.readline().split()))
know.pop(0)

arr=[]
dp=[True]*M

for _ in range(M):
  temp=list(map(int,sys.stdin.readline().split()))
  temp.pop(0)
  arr.append(temp)


for k in know:
  for j in range(M):
    if not dp[j]:
      continue
    if k in arr[j]:
      for a in arr[j]:
        if a not in know:
          know.append(a)
      dp[j]=False
      continue

print(dp.count(True))


