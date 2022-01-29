def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()
    
    # [5, 3]인 경우, 2가 return 되어야 함
    if citations[0] > n :
        return n
    
    for i in range(1, n+1) :
        if citations[-i] < i: 
            return i - 1
    
    return answer