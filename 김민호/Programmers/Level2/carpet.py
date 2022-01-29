def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for i in range(1, total+1):
        if total % i != 0:
            continue
        
        width = i
        height = total // i
        
        if ((width + height) * 2 - 4) == brown and ((width-2) * (height - 2)) == yellow:
            answer.append(width)
            answer.append(height)
            answer.sort(reverse=True)
            break
    
    return answer