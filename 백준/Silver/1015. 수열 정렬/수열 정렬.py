import sys

N=int(sys.stdin.readline())

A=list(map(int,sys.stdin.readline().split()))

arr=[]

for i in range(N):
  arr.append([i,A[i]])

arr.sort(key=lambda x:x[1])

for i in range(N):
  arr[i].append(i)

arr.sort()

for i in range(N):
  sys.stdout.write(str(arr[i][2])+' ')

print()