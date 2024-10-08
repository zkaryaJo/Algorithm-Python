def solution(num_list):
    answer = 0
    
    #1. 모든 원소들의 곱
    # 리스트를 * 들어간 문자로 바꾸기
    
    str_list = [str(i) for i in num_list]  #'3', '4', '5', '2', '1'
    str_list = '*'.join(str_list) #'3*4*5*2*1'
    
    # eval 적용하여 계산하기 : eval(str_list)
    
    
    #모든 원소들의 합의 제곱 : sum(num_list)**2
    
    return 1 if eval(str_list) < sum(num_list)**2 else 0