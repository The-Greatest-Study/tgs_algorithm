# 망할 효율성.... 나중에 다시 효율성 체크해라 오지인
def solution(info, query):
    answer = []
    
    applicants = []
    for string in info :
        applicant = string.split(' ')
        applicants.append(applicant)
    
    questions = []
    for q in query : 
        question = q.split(' and ')
        last = question[-1]
        question = question[:-1]
        last_list = last.split(' ')
        question.append(last_list[0])
        question.append(last_list[1])
        questions.append(question)
        answer.append(0)
    
    for person in applicants :
        for i in range(len(answer)) :
            question = questions[i]
            person_score = int(person[-1])
            score = int(question[-1])
            
            # 코딩테스트 기준 점수보다 낮은 경우 제외
            if person_score < score :
                continue
            
            # 코딩테스트 기준을 넘었다면 그 외 기준 체크
            flag = True
            for j in range(4) :
                condition = question[j]
                if condition == '-' :
                    continue
                if condition != person[j] :
                    flag = False
                    break
            if flag :
                answer[i] += 1
    
    return answer