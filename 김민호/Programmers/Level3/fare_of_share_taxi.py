from math import inf

def solution(n, s, a, b, fares):
    answer = inf
    
    cost = [[inf] * n for j in range(n)]
    
    for p, q, c in fares:
        cost[p-1][q-1] = c
        cost[q-1][p-1] = c
    
    for i in range(n):
        cost[i][i] = 0
        
    for c in range(n):
        for i in range(n):
            for j in range(n):
                if i != j and i < j:
                    if cost[i][j] > cost[i][c] + cost[c][j]:
                        cost[i][j] = cost[i][c] + cost[c][j]
                    cost[j][i] = cost[i][j]
    
    for i in range(n):
        if answer > cost[s-1][i] + cost[i][a-1] + cost[i][b-1]:
            answer = cost[s-1][i] + cost[i][a-1] + cost[i][b-1]
    
    return answer