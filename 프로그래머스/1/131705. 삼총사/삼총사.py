import itertools

def solution(number):
    
    answer = 0
    
    comb = itertools.combinations(number, 3)
    
    #[(-2, 3, 0), (-2, 3, 2), (-2, 3, -5), (-2, 0, 2), (-2, 0, -5), (-2, 2, -5), (3, 0, 2), (3, 0, -5), (3, 2, -5), (0, 2, -5)]
    l = list(comb)
    
    #튜플의 합이 0인 item 갯수만 뽑아서 배열로 변환 후 배열의 사이즈 계산.
    answer = len([item for item in l if sum(item) == 0])
        
    return answer