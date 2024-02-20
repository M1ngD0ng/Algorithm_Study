max_len = len(bin(10**16)[2:])
dp = [0 for _ in range(max_len)]
dp[0] = 1
for i in range(max_len):
    dp[i] = 2 * dp[i-1] + (1<<i) # 초기값, i 번째 자리수까지 1의 합

def suffix_sum(x):
    ans = x & 1 # 0 번째 자리 수
    for i in range(max_len, 0, -1): # 가장 높은 자리 수 부터 
        if x & 1 << i: # x가 i 번째 자리에 값을 가지고 있다면
            ans += dp[i-1] + x - (1<<i) + 1 # 1의 수 계산
            x -= 1<<i # 가장 높은 자리의 1의 수는 계산 되었으므로 제거
    return ans

A, B = map(int, input().split())
print(suffix_sum(B) - suffix_sum(A-1))