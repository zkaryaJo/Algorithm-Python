def solution(s, skip, index):
    answer = ''
    
    #set은 차집합 연산 가능
    alpha_sub_skip = set("abcdefghijklmnopqrstuvwxyz") - set(skip)
    
    #문자열 정렬을 위한 list화
    alpha_sub_skip = list(alpha_sub_skip)
    
    alpha_sub_skip.sort()
    
    str_alpha = ''.join(alpha_sub_skip)
    
    for i, item in enumerate(s) :
        idx = (str_alpha.find(item)+index) % len(str_alpha)
        #print(item, idx)
        
        answer +=str_alpha[idx]
    
    print(alpha_sub_skip)
    
    
    return answer