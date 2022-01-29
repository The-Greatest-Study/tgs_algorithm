def checkRight(s):
    flag = False
    tmp = 0
    checked = 0
    s_list = []
    
    for i, c in zip(range(len(s)), s):
        if c == "(":
            tmp += 1
        else:
            tmp -= 1
        
        if tmp == 0:
            checked = i + 1
        elif tmp < 0:
            s_list = list(s)
            return [False, s_list[:i], s_list[i:]]
    
    if tmp == 0:
        return [True, "", ""]
    else:
        flag = False
    return [flag, s_list[:checked], s_list[checked:]]

def solution(p):
    answer = ''
    
    if p == "":
        return answer;
    
    while True:
        flag, u, v = checkRight(p)
    
    return answer