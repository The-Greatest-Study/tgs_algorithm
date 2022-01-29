def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    find_flag = False
    for i in range(len(completion)) :
        if participant[i] != completion[i] :
            answer = participant[i]
            find_flag = True
            break
    if not find_flag :
        answer = participant[-1]
    
    return answer