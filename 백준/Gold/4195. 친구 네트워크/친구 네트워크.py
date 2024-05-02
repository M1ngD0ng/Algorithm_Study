import sys

T = int(sys.stdin.readline())


def find(x):
  if parent[x][0] != x:
    parent[x][0] = find(parent[x][0])
  return parent[x][0]


def union(a, b):
  a = find(a)
  b = find(b)
  temp = parent[a][1] + parent[b][1]

  if a != b:
    parent[b][0] = a
    parent[a][1] = temp
  # elif b < a:
  #   parent[a][0] = b
  #   parent[b][1] = temp
  else:
    return parent[a][1]
  return temp


for _ in range(T):
  F = int(sys.stdin.readline())
  parent = []
  idx = -1
  nameDict = dict()
  for _ in range(F):
    A, B = sys.stdin.readline().split()
    if (A not in nameDict.keys()) and (
        B not in nameDict.keys()):  # 둘 다 없으면 A를 더 상위노드로 둠
      idx += 1
      nameDict[A] = idx
      idx += 1
      nameDict[B] = idx

      parent.append([nameDict[A], 2])
      parent.append([nameDict[A], 2])
      print(2)
    elif (A in nameDict.keys()) and (B not in nameDict.keys()):
      idx += 1
      nameDict[B] = idx

      paAB = find(nameDict[A])  # A,B의 부모가 될 노드의 인덱스를 찾음
      parent[paAB][1] += 1  # B까지 연결되어 1추가
      parent.append([paAB, parent[paAB][1]])
      print(parent[paAB][1])
    elif (B in nameDict.keys()) and (A not in nameDict.keys()):
      idx += 1
      nameDict[A] = idx

      paAB = find(nameDict[B])  # A,B의 부모가 될 노드의 인덱스를 찾음
      parent[paAB][1] += 1  # B까지 연결되어 1추가
      parent.append([paAB, parent[paAB][1]])
      print(parent[paAB][1])
    else:  # 둘다 이미 들어왔었던 이름일 때
      print(union(nameDict[A], nameDict[B]))
