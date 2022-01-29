import itertools
# 'ABCDEFG' 'HIJKLMNOP' 이런 경우 combination 생각하면... 
def solution(orders, course):
    answer = []
    for i in range(len(orders)) :
        order = orders[i]
        orders[i] = ''.join(sorted(order))
    
    for n in course :
        possible = []   # possible : 가능한 코스 조합 (tuple)
        for order in orders :
            temp = list(itertools.combinations(order, n))
            for t in temp : 
                if t not in possible :
                    possible.append(t)
        count = {}
        now = ''
        for poss in possible :
            now = ''.join(poss)                             # now : 가능한 코스 조합 (string)
            count[now] = 0                                  # count : 해당 코스 조합이 몇 번 나오는지 카운팅한 dictionary
            flag = True
            for order in orders :
                for menu in poss :
                    flag = menu in order                    # 해당 메뉴가 order에 없으면 false
                    if not flag :
                        break
                if flag :                                   # 코스 조합이 다 있으면 count[now] += 1
                    count[now] += 1
        if not count :
            continue
        max_count = max(count.values())
        if max_count < 2 :                                  # 2번 미만인 경우 코스에 추가하면 안 됨
            continue
        keys = list(count.keys())
        for key in keys :
            if max_count == count[key] :
                answer.append(key)
    
    answer.sort()                                           # 사전 순으로 정렬
    return answer