def solution(answers):
    answer = []
    n = len(answers)
    
    student_1 = [1,2,3,4,5]
    student_2 = [2,1,2,3,2,4,2,5]
    student_3 = [3,3,1,1,2,2,4,4,5,5]
    
    mul_1 = min(int(n/5) + 1, 2000)
    mul_2 = min(int(n/8) + 1, 1250)
    mul_3 = min(int(n/10) + 1, 1000)
    
    student_1 *= mul_1
    student_2 *= mul_2
    student_3 *= mul_3
    
    count_1 = 0
    count_2 = 0
    count_3 = 0
    
    for i in range(n) :
        if student_1[i] == answers[i] :
            count_1 += 1
        if student_2[i] == answers[i] :
            count_2 += 1
        if student_3[i] == answers[i] :
            count_3 += 1
    
    m = max(count_1, count_2, count_3)
    
    if m == count_1 :
        answer.append(1)
    if m == count_2 :
        answer.append(2)
    if m == count_3 :
        answer.append(3)
    
    return answer