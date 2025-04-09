def solution(board, moves):
    answer = 0
    
    stack=[]
    N=len(board)
    
    for m in moves:
        for i in range(N):
            if board[i][m-1]!=0:
                if stack and stack[-1]==board[i][m-1]:
                    stack.pop()
                    answer+=2
                else:
                    stack.append(board[i][m-1])
                board[i][m-1]=0
                
                break
            
    return answer