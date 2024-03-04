import sys
N=int(sys.stdin.readline())
M=int(sys.stdin.readline())

A=list(map(int,sys.stdin.readline().split()))
_min=abs(100-N)

for i in range(1000001):
  i=str(i)

  for j in range(len(i)):
    if int(i[j]) in A:
      break
    elif j==len(i)-1:
      _min=min(_min,abs(int(i)-N)+len(i))

print(_min)