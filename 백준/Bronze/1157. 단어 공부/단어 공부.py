import sys
A=list(sys.stdin.readline().rstrip().upper())

dp=dict()
for a in A:
  if a not in dp.keys():
    dp[a]=A.count(a)

m=max(dp.values()) 
temp=[]
for k,v in dp.items():
  if v==m:
    temp.append(k)
 
if len(temp)==1:
  print(temp[0])
else:
  print("?")