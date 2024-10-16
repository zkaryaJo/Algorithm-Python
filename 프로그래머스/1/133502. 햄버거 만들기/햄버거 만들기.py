def solution(ingredient):
    answer = 0
    
#    문자열로 합치기
#     a = ''.join(str(c) for c in ingredient)
    
#     #1231 패턴을 앞에서 부터 찾아서 소거하기
#     while(a.find('1231') > 0):
#         index = a.find('1231')
#         left = a[:index]
#         right = a[index+4:]
#         a = left + right
        
#         answer += 1
    
    s = []
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1,2,3,1]:
            answer += 1
            for _ in range(4):
                s.pop()
    
    
    return answer