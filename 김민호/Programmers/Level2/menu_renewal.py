from itertools import combinations
import operator

def solution(orders, course):
    answer = []
    set_list_cnt = {}
    
    for order in orders:
        order_list = list(order)
        for num in course:
            menu_comb = combinations(order_list, num)
            for menu in menu_comb:
                menu = list(menu)
                menu.sort()
                menu_str = "".join(menu)
                if menu_str not in set_list_cnt:
                    set_list_cnt[menu_str] = 1
                else:
                    set_list_cnt[menu_str] += 1
            
    sorted_dict = sorted(set_list_cnt.items(), key=operator.itemgetter(1) ,reverse=True)
    
    for num in course:
        max = -1
        for menu, cnt in sorted_dict:
            if cnt < 2:
                continue
            
            if len(menu) == num:
                if max == -1:
                    max = cnt
                    answer.append(menu)
                elif max == cnt:
                    answer.append(menu)
    
    answer.sort()
    
    return answer