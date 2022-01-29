def solution(phone_book):
    answer = True

    phone_book.sort()

    for phone1, phone2 in zip(phone_book, phone_book[1:]):
        if phone2.startswith(phone1):
            return False

    return answer