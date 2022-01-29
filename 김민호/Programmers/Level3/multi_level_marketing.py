def solution(enroll, referral, seller, amount):
    answer = []
    links = {}
    value_dic = {"center":0}
    
    for e, r in zip(enroll, referral):
        if e not in links:
            links[e] = ""
        
        if r == "-":
            links[e] = "center"
        else:
            links[e] = r
        
        value_dic[e] = 0
    
    for s, a in zip(seller, amount):
        loc = s
        tmp_dic = {s:a*100}
        
        while loc != "center":
            if tmp_dic[loc] * 0.1 < 1:
                break
            else:
                if links[loc] != "":
                    tmp_dic[links[loc]] = int(tmp_dic[loc] * 0.1)
                    tmp_dic[loc] = tmp_dic[loc] - tmp_dic[links[loc]]
                    loc = links[loc]
                else:
                    loc = "center"
        
        for key, value in tmp_dic.items():
            value_dic[key] += value
    
    for e in enroll:
        answer.append(value_dic[e])
    
    return answer