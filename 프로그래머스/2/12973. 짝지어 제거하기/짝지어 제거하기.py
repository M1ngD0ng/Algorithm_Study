def solution(s):
    stack=[]
    
    for c in s:
        if not stack:
            stack.append(c)
        else:
            if stack[-1]==c:
                stack.pop()
            else:
                stack.append(c)
                
    if not stack:       
        return 1
    return 0