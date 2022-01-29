def solution(new_id):
    id_length = len(new_id)
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    special_char = ['-', '_', '.']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    def is_valid(s):
        if s in alpha or s in special_char or s in num:
            return True
        else:
            return False
        
    id_list = list(new_id)
    new_id_list = [x for x in id_list if is_valid(x)]
    new_id = "".join(new_id_list)
    
    # 3단계
    tmp = ""
    id_list = list(new_id)
    token = ""
    
    for s in id_list:
        if s == ".":
            if token == "":
                token = "."
        else:
            if token == ".":
                tmp += token
                tmp += s
                token = ""
            else:
                tmp += s
                
    new_id = tmp
    
    # 4단계
    id_list = list(new_id)
    for i, s in zip(range(len(id_list)),id_list):
        if s == ".":
            id_list[i] = ""
        else:
            break
    
    for i, s in zip(range(len(id_list)),id_list):
        if id_list[-i] == ".":
            id_list[-i] = ""
        else:
            break
    
    new_id = "".join(id_list)
    
    # 5단계
    if new_id == "":
        new_id = "a"
        
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        
    while new_id[-1] == ".":
        new_id = new_id[:-1]
        
    # 7단계
    if len(new_id) <= 2:
        char = new_id[-1]
        while len(new_id) < 3:
            new_id += char
    
    return new_id