def solution(rows, columns, queries):
    answer = []
    map = [[i+1+j*columns for i in range(columns)] for j in range(rows)]
    
    for query in queries:
        width = query[3] - query[1]
        height = query[2] - query[0]
        x1 = query[1] - 1
        x2 = query[3] - 1
        y1 = query[0] - 1
        y2 = query[2] - 1
        tmp = []
        
        cur_x = -1
        cur_y = -1
        min = 10001
        
        while cur_x != x1 or cur_y != y1:
            if cur_x == -1 and cur_y == -1:
                cur_x = x1
                cur_y = y1
                
            if cur_y == y1:
                if cur_x + 1 <= x2:
                    tmp.append([cur_y, cur_x + 1, map[cur_y][cur_x]])
                    cur_x += 1
                else:
                    tmp.append([cur_y + 1, cur_x, map[cur_y][cur_x]])
                    cur_y += 1
            elif cur_y == y2:
                if cur_x - 1 >= x1:
                    tmp.append([cur_y, cur_x - 1, map[cur_y][cur_x]])
                    cur_x -= 1
                else:
                    tmp.append([cur_y - 1, cur_x, map[cur_y][cur_x]])
                    cur_y -= 1
            else:
                if cur_x == x1:
                    tmp.append([cur_y - 1, cur_x, map[cur_y][cur_x]])
                    cur_y -= 1
                elif cur_x == x2:
                    tmp.append([cur_y + 1, cur_x, map[cur_y][cur_x]])
                    cur_y += 1
            if map[cur_y][cur_x] < min:
                min = map[cur_y][cur_x]
        
        for q, p, v in tmp:
            map[q][p] = v
        
        answer.append(min)
    return answer