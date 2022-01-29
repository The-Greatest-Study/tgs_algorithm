from functools import reduce

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    answer = reduce(lambda x,y: x+y, numbers)
    answer = int(answer)
    
    return str(answer)