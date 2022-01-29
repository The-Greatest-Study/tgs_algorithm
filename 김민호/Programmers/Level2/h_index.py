def solution(citations):
    answer = 0
    citations.sort()
    length = len(citations)
    
    for i, citation in zip(range(length),citations):
        if citation >= length - i:
            answer = length - i
            break
    
    return answer