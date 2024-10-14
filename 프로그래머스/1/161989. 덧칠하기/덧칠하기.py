def solution(n, m, section):
    
    answer = 0
    last = 0
    
    for i in section:
        if i > last:
            last = i+m-1
            answer += 1

    return answer