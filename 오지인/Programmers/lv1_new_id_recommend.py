import re

def solution(new_id):
    answer = new_id
    
    # Step 1
    answer = answer.lower()
    
    # Step 2
    answer = re.sub('[^a-z0-9._-]', '', answer)
    
    # Step 3
    answer = re.sub('[.]+', '.', answer)    # '.' 연속 시 하나의 '.'으로 치환
    
    # Step 4
    answer = re.sub('^[.]', '', answer)     # 맨 앞의 . 제거
    answer = re.sub('[.]$', '', answer)     # 맨 뒤의 . 제거
    
    # Step 5
    if not answer :
        answer = 'a'
        
    # Step 6
    if len(answer) > 15 :
        answer = answer[0:15]
    answer = re.sub('[.]$', '', answer)     # 길이 줄인 후 맨 뒤의 . 제거
    
    # Step 7
    if len(answer) < 3 :
        answer += answer[-1] * (3-len(answer))
        
    return answer