import sys

V,E=map(int,sys.stdin.readline().split())
parent=[0]*(V+1)

for i in range(1,V+1):
  parent[i]=i

# 특정 원소가 속한 집합을 찾기
def find(x):
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x]!=x:
    parent[x]=find(parent[x])
  return parent[x]

def union(a,b):
  a=find(a)
  b=find(b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

for i in range(E):
  a,b=map(int,sys.stdin.readline().split())
  union(a,b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1,V+1):
  print(find(i), end='')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1,V+1):
  print(parent[i], end='')
