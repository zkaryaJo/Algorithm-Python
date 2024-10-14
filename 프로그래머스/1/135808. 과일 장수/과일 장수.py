def solution(k, m, score):
    answer = 0
    
    #1. 작은 순서대로 정렬
    score.sort()
        
    #2. 남는 사과는 버려야 하므로 시작인덱스를 뒤에서부터
    startIndex = len(score)%m
    lastIndex = len(score)
    
    for i in range(startIndex, lastIndex, m):
        answer += m * score[i]
    
    return answer