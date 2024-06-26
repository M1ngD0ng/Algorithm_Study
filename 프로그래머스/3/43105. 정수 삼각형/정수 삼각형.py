def solution(T):
    N=len(T)
    
    dp=[[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1):
            dp[i].append(0)
        
    dp[0][0]=T[0][0]
    
    for i in range(1,N):
        for j in range(i+1):
            if j==0:
                dp[i][j]=dp[i-1][j]+T[i][j]
            elif j==i:
                dp[i][j]=dp[i-1][j-1]+T[i][j]
            else:
                dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+T[i][j]
    
            
    return max(dp[N-1])