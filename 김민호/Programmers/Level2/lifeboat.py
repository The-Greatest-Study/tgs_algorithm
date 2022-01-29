def solution(people, limit):
    answer = 0
    people.sort()
    front = 0
    back = len(people) - 1
    
    while front <= back:
        answer += 1
        if people[front] + people[back] <= limit:
            front += 1
        
        back -= 1
    
    return answer