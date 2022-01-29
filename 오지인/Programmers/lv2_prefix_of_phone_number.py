#지인아 효율성은 언제 볼꺼니?
def solution(phone_book):
    answer = True
    
    phone_book.sort()
    sorted(phone_book, key=lambda x : len(x))
    
    n = len(phone_book)
    for i in range(n) :
        temp = phone_book[i+1:]
        for j in range(i+1, n) :
            if phone_book[j].startswith(phone_book[i]) :
                answer = False
                break
    
    return answer