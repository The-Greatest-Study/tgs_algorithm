def solution(lottos, win_nums):
    answer = []
    wrong = 0
    zero = 0
    
    for lotto in lottos:    
        if lotto != 0 and win_nums.count(lotto) == 0:
            wrong += 1
        elif lotto == 0:
            zero += 1
        
    answer.append(1+wrong)
    answer.append(1+wrong+zero)
    
    if answer[0] > 6:
        answer[0] = 6
    
    if answer[1] > 6:
        answer[1] = 6
    
    return answer