def gcd(a,b):
    # 유클리드 호제법
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    
    return a

def solution(w,h):
    answer = w * h
    
    return w * h - (w + h - gcd(w, h))