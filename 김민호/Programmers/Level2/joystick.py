def solution(name):
    answer = 0
    alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    alpha_dict = {}
    name_list = list(name)
    name_length = len(name_list)
    check_list = ["A" for i in range(name_length)]
    cur_idx = 0
    
    for i in range(26):
        alpha_dict[alphabets[i]] = min(i, 26-i)
    
    for i in range(name_length):
        front = cur_idx + i if (cur_idx + i) < name_length else (cur_idx + i - name_length)
        back = cur_idx - i if (cur_idx - i) >= 0 else (cur_idx - i + name_length)
    
    while "".join(check_list) != name:
        for i in range(name_length):
            front = cur_idx + i if cur_idx + i < name_length else cur_idx + i - name_length
            back = cur_idx - i if cur_idx - i >= 0 else cur_idx - i + name_length
            
            if alpha_dict[name_list[front]] == 0:
                front = 21
            if alpha_dict[name_list[back]] == 0:
                back = 21
            
            if front != 21 and back != 21:
                new_idx = front if alpha_dict[name_list[front]] <= alpha_dict[name_list[back]] else back
                cur_idx = new_idx
                check_list[new_idx] = name_list[new_idx]
                answer += alpha_dict[name_list[new_idx]]
                name_list[new_idx] = "A"
                break
            elif front != 21 or back != 21:
                new_idx = min(front, back)
                cur_idx = new_idx
                check_list[new_idx] = name_list[new_idx]
                answer += alpha_dict[name_list[new_idx]]
                name_list[new_idx] = "A"
                break
            else:
                answer += 1
    return answer