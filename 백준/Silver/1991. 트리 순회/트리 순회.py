import sys

N=int(sys.stdin.readline())
d=dict()

for _ in range(N):
  a,b,c=sys.stdin.readline().split()
  d[a]=[b,c] 

ans=[[] for _ in range(3)]

def first(node):
  ans[0].append(node)
  if d[node]:
    for i in d[node]:
      if i=='.':
        continue
      first(i)

first('A')
for i in ans[0]:
  sys.stdout.write(i)
print()

def second(node):
  if d[node][0]!='.':
    second(d[node][0])
  ans[1].append(node)
  if d[node][1]!='.':
    second(d[node][1])


second('A')
for i in ans[1]:
  sys.stdout.write(i)

print()

def third(node):
  for i in d[node]:
    if i=='.':
      continue
    third(i)
    ans[2].append(i)


third('A')
ans[2].append('A')
for i in ans[2]:
  sys.stdout.write(i)
print()
