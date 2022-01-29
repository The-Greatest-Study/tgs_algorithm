answer = 0

def search(idx,total,numbers,target):
    global answer
    if idx >= len(numbers):
        if total == target:
            answer += 1
            return
        else:
            return
    
    try:
        search(idx+1,total+numbers[idx],numbers,target)
        search(idx+1,total-numbers[idx],numbers,target)
    except IndexError:
        return

def solution(numbers, target):
    global answer
    search(0,0,numbers,target)
    
    return answer