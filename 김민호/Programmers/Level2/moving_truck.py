def solution(bridge_length, weight, truck_weights):
    answer = 0
    load = [0 for i in range(bridge_length)]
    
    while truck_weights or sum(load) > 0:
        answer += 1
        load.pop(0)
        
        if truck_weights:
            if sum(load) + truck_weights[0] <= weight:
                load.append(truck_weights.pop(0))
            else:
                load.append(0)
        else:
            load.append(0)
        
    return answer