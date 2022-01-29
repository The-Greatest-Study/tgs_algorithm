from itertools import combinations

def solution(info, query):
    answer = []
    info_dic = {}
    
    for employee in info:
        emp_list = employee.split(" ")
        kinds = emp_list[:-1]
        score = int(emp_list[-1])
        
        for i in range(5):
            comb = combinations(range(4), i)
            
            for c in comb:
                tmp_list = kinds.copy()
                
                for idx in c:
                    tmp_list[idx] = "-"
                
                tmp_str = " and ".join(tmp_list)
                
                if tmp_str in info_dic:
                    info_dic[tmp_str].append(score)
                else:
                    info_dic[tmp_str] = [score]
    
    for value in info_dic.values():
        value.sort()
    
    for q_str in query:
        q_list = q_str.split(" ")
        score = int(q_list[-1])
        q_list = q_list[:-1]
        q_str = " ".join(q_list)
        
        if q_str not in info_dic:
            answer.append(0)
            continue
            
        values = info_dic[q_str]
                
        length = len(values)  
        start, end = 0, length
        
        while start != end and start != length:
            cur = (start+end) // 2
            if values[cur] >= score:
                end = cur
            else:
                start = cur + 1
        
        
        answer.append(length - start)
        
    return answer