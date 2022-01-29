def solution(s):
    answer = -1
    s = list(s)
    stack = []
    last = ""
    
    for c in s:
        if last == "":
            last = c
            stack.append(c)
        else:
            if last == c:
                stack.pop()
                if len(stack) > 0:
                    last = stack[-1]
                else:
                    last = ""
            else:
                last = c
                stack.append(c)
        
    if len(stack) > 0:
        answer = 0
    else:
        answer = 1
        
    return answer