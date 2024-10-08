def solution(numLog):
    answer = ''
    
    prev_list = numLog[:-1]
    next_list = numLog[1:]
    
    arr = [n-p for p, n in zip(prev_list, next_list)] #증분값 배열 구하기
    
    for i in arr:
        if(i == 1):
            answer+='w'
        elif(i==-1):
            answer+='s'
            
        elif(i==10):
            answer+='d'
        else:
            answer+='a'
    
    return answer