from itertools import permutations

def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

def solution(numbers):
    answer = 0
    number_list = list(numbers)
    length = len(number_list)
    finded_num = []
    
    for i in range(1, length + 1):
        number_p = permutations(number_list, i)

        for p in number_p:
            cur_num = int("".join(p))
            
            if cur_num not in finded_num:
                finded_num.append(cur_num)
    
    for cur in finded_num:
        if cur < 2:
            continue
        elif check_prime(cur) == True:
            answer += 1
    
    return answer