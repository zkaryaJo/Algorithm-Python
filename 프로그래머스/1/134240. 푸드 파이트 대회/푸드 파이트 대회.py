def solution(food):
    answer = ''
    left = ''
    right = ''
    
    for i, n in enumerate(food[1:]):
        d = i+1
        if i >=  0 :
            s = str(d)*(n//2)
            left    = left + s
            right   = s + right
    
    answer = left +'0'+ right
    
    return answer