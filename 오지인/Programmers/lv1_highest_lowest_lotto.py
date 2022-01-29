def solution(lottos, win_nums):
    answer = []
    
    count_zero = 0
    count_win = 0
    
    for lotto in lottos : 
        if lotto in win_nums :
            count_win += 1
        if lotto == 0 :
            count_zero += 1
    
    answer.append(min(7-count_win-count_zero, 6))
    answer.append(min(7-count_win, 6))
        
    return answer