def solution(prices):
    price_len = len(prices)
    answer = [0 for i in range(price_len)]
    
    for i in range(price_len-1):
        cnt = 1
        for j in range(i+1, price_len-1):
            if prices[j] >= prices[i]:
                cnt += 1
            else:
                break
        answer[i] = cnt
            
    answer[price_len-1] = 0
    
    return answer