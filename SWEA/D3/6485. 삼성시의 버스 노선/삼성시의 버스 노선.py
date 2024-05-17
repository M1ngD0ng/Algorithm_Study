T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    dp=[0]*(5001)
    for _ in range(1,N+1):
        A,B=map(int,input().split())
        for i in range(A,B+1):
            dp[i]+=1

    P=int(input())
    print(f'#{test_case}',end=" ")
    for _ in range(P):
        C=int(input())
        print(dp[C],end=" ")

    print()
