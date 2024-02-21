T = int(input())
answer = []

#dp[n] = [최솟값, 최댓값]
dp = [0, 0, [1, 1], [7, 7], [4, 11], [2, 71], [6, 111], [8, 711], [10, 1111], [18, 7111], [22, 11111]]

#p[n%3]: 0, 1, 2, 4, 5 -> 최솟값 =  p[n%3] + '8'*(n//7-1)
#p[n%3] = 3 -> 최솟값 = p[n%3] + '8'*(n//7-2)
p = ['8', '10', '18', '200', '20', '28', '68']

for _ in range(T):
    n = int(input())
    
    #n이 10 이하인 경우
    if n < len(dp):
        answer.append(dp[n])
        continue
        
    #최댓값 구하기
    #n이 짝수인 경우
    if n%2==0:
        max = '1'*(n//2)
    #n이 홀수인 경우
    else:
        max = '7' + '1'*((n-3)//2)
        
    #최솟값 구하기
    pivot = n%7
    if pivot == 3:
        min =  p[pivot] + '8'*(n//7-2)
        answer.append([int(min), int(max)])
        continue
    #pivot: 0, 1, 2, 4, 5
    min = p[pivot]+'8'*(n//7-1)
    answer.append([int(min), int(max)])
    
for i in range(len(answer)):
    print(answer[i][0], answer[i][1])
#시간복잡도 = O(T), 공간복잡도 = O(T)