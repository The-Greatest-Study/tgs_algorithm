
def solution(clothes):
    answer = 0
    sorted_cloth = {}

    for cloth in clothes:
        if sorted_cloth.get(cloth[1]):
            sorted_cloth[cloth[1]] += 1
        else:
            sorted_cloth[cloth[1]] = 2

    for key in sorted_cloth.keys():
        if answer == 0:
            answer += sorted_cloth[key]
        else:
            answer *= sorted_cloth[key]

    return answer-1

# 시간 초과 버전
"""
from itertools import combinations
def solution(clothes):
    answer = 0
    sorted_cloth = {}

    for cloth in clothes:
        if sorted_cloth.get(cloth[1]):
            sorted_cloth[cloth[1]].append(cloth[0])
        else:
            sorted_cloth[cloth[1]] = [cloth[0]]

    for i in range(1,len(sorted_cloth)+1):
        key_list = [k for k in sorted_cloth.keys()]
        combs = combinations(key_list,i)
            
        for comb in combs:
            value = 1
                
            for key in comb:
                value *= len(sorted_cloth[key])
                
            answer += value

    return answer
"""