import sys
P,M=map(int,sys.stdin.readline().split())

room=[]
name=dict()
for _ in range(P):
  a,b=sys.stdin.readline().split() 
  name[b]=int(a)
  isIn=False
  if room:
    for i in range(len(room)):
      if len(room[i])==M:
        continue
      elif (name[room[i][0]]-10)<=name[b]<=(name[room[i][0]]+10):
        room[i].append(b)
        isIn=True
        break
  if not isIn:
    room.append([b])
  
for i in range(len(room)):
  if len(room[i])==M:
    print("Started!")
  else:
    print("Waiting!")
  temp=sorted(room[i])
  for j in temp:
    print(name[j],j)

