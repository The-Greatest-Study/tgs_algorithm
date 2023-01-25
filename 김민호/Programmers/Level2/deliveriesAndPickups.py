from collections import deque

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    dels = deque()
    picks = deque()
    
    # 유효한 배달, 수거 재활용 택배 queue
    for i, d, p in zip(range(n), deliveries, pickups):
        if d != 0:
            dels.append([i+1, d])
        
        if p != 0:
            picks.append([i+1, p])
            
    dels.reverse()
    picks.reverse()
    
    while dels or picks:
        loads = [0, 0]
        length = 0
        
        # 배달 최대길이
        while loads[0] < cap and dels:
            l, d = dels.popleft()
            
            if loads[0] + d > cap:
                d = loads[0] + d - cap
                loads[0] = cap
                dels.appendleft([l,d])
            elif loads[0] + d == cap:
                loads[0] = cap
            else:
                loads[0] += d
            
            if l > length:
                length = l
        
        # 수거 최대길이
        while loads[1] < cap and picks:
            l, d = picks.popleft()
            
            if loads[1] + d > cap:
                d = loads[1] + d - cap
                loads[1] = cap
                picks.appendleft([l,d])
            elif loads[1] + d == cap:
                loads[1] = cap
            else:
                loads[1] += d
            
            if l > length:
                length = l
        
        # 배달, 수거의 최대길이의 2배
        answer += length * 2
            
    return answer