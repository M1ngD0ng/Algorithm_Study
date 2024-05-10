T=int(input())

for i in range(1,T+1):
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort()
    _min=1e10
    for j in range(K-1,N):
        _min=min(_min,A[j]-A[j-K+1]) 

    print(f'#{i} {_min}')