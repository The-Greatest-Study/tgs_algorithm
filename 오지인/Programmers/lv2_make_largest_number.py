def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        # stack이 비워져 있으면 채우기
        if not answer:
            answer.append(num)
            continue
        
        # stack의 마지막 값 < 새롭게 stack에 들어갈 값 => pop해서 없애주기
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)
        
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)