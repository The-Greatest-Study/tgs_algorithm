import copy

def solution(priorities, location):
    answer = 0
    workloads = []
    priority_rank = sorted(copy.deepcopy(priorities), reverse=True)
    
    for idx, priority in zip(range(len(priorities)), priorities):
        if idx == location:
            workloads.append([priority, True])
        else:
            workloads.append([priority, False])
            
    while workloads:
        
        cur = workloads.pop(0)
        
        if cur[0] < priority_rank[0]:
            workloads.append(cur)
        else:
            answer += 1
            if cur[1]:
                return answer
            else:
                priority_rank.pop(0)
                
    
    return answer