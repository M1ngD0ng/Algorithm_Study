import sys
A=[]
for _ in range(5):
  n=int(sys.stdin.readline())
  if n<40:
    A.append(40)
  else:
    A.append(n)
  
print(sum(A)//5)