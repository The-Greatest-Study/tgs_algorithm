def solution(n, lost, reserve):
    answer = 0
    
    status = [0] * n
    
    for person in lost : 
        status[person - 1] -= 1
    
    for person in reserve : 
        status[person - 1] += 1
    
    for index in range(n) :
        prev_idx = max(index-1, 0)
        next_idx = min(index+1, n-1)
        if status[index] < 0 :
            if status[prev_idx] > 0 :
                status[prev_idx] -= 1
                status[index] += 1
                answer += 1
            elif status[next_idx] > 0 :
                status[next_idx] -= 1
                status[index] += 1
                answer += 1
        else :
            answer += 1
    
    return answer