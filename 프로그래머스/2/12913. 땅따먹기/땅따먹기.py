def solution(land):
    answer = 0
    N=len(land)
    
    dp=[[0]*4 for _ in range(N)]
    for i in range(4):
        dp[0][i]=land[0][i]
        
    for i in range(1,N):
        for j in range(4):
            dp[i][j]=land[i][j]
            for k in range(4):
                if j==k: continue
                dp[i][j]=max(dp[i][j], dp[i-1][k]+land[i][j])
    
    return max(dp[-1])