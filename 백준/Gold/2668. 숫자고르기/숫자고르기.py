import sys

N=int(sys.stdin.readline())

dp=[False]*(N+1)
d=dict()
for i in range(N):
  d[i+1]=int(sys.stdin.readline())

while True:
  temp=[]
  for a in d.keys():
    if a not in d.values():
      temp.append(a)
  if not temp:
    break
  for t in temp:
    d.pop(t)

print(len(d))
for i in d.keys():
  print(i)