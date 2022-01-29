def solution(rows, columns, queries):
    answer = []
    
    # make matrix
    matrix = []
    start = 1
    for i in range(rows) :
        temp_row = []
        for j in range(columns) :
            temp_row.append(start)
            start += 1
        matrix.append(temp_row)
    
    for query in queries :
        start_row = query[0] - 1
        start_col = query[1] - 1
        final_row = query[2] - 1
        final_col = query[3] - 1
        
        min_num = rows * columns
        start = matrix[start_row][start_col]
        if min_num > start :
            min_num = start
        # print(start_row, start_col, final_row, final_col)
        for i in range(start_row, final_row) :
            # print('[', i, ']', '[', start_col, ']')
            matrix[i][start_col] = matrix[i+1][start_col]
            if min_num > matrix[i][start_col] :
                min_num = matrix[i][start_col]
        for j in range(start_col, final_col) :
            # print('[', final_row, ']', '[', j, ']')
            matrix[final_row][j] = matrix[final_row][j+1]
            if min_num > matrix[final_row][j] :
                min_num = matrix[final_row][j]
        for i in range(final_row, start_row, - 1) :
            # print('[', i, ']', '[', final_col, ']')
            matrix[i][final_col] = matrix[i-1][final_col]
            if min_num > matrix[i][final_col] :
                min_num = matrix[i][final_col]
        for j in range(final_col, start_col, -1) :
            # print('[', start_row, ']', '[', j, ']')
            matrix[start_row][j] = matrix[start_row][j-1]
            if min_num > matrix[start_row][j] :
                min_num = matrix[start_row][j]
        matrix[start_row][start_col+1] = start
        # 가장 작은 수 answer에 추가
        answer.append(min_num)
    
    return answer