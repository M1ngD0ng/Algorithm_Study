import sys
N=int(sys.stdin.readline())

A=set()
for _ in range(N):
  t= sys.stdin.readline()

  if t[1]=='d':
    s,x=t.split() 
    A.add(int(x))
  elif t[1]=='e':
    s,x=t.split()
    if int(x) in A:
     A.remove(int(x))
  elif t[1]=='h':
    s,x=t.split()
    if int(x) in A:
      print(1)
    else:
      print(0)
  elif t[1]=='o':
    s,x=t.split()
    if int(x) in A:
      A.remove(int(x))
    else:
      A.add(int(x))
  elif t[1]=='l':  
    A={ i for i in range(1,21)}
  elif t[1]=='m':
    A.clear()