def solution(progresses, speeds):
    answer = []
    need_times = []
    days = 0
    cnt = 0
    
    for progress, speed in zip(progresses, speeds):
        tmp = 0
        if (100 - progress) % speed == 0:
            tmp = (100 - progress) // speed
        else:
            tmp = (100 - progress) // speed + 1
        need_times.append(tmp)
    
    for need_time in need_times:
        if need_time > days:
            days = need_time
            if cnt > 0:
                answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
    
    if cnt > 0:
        answer.append(cnt)
    
    return answer