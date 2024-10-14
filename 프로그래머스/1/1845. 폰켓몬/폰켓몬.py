import itertools
def solution(nums):
    takes = int(len(nums)/2) #종류가 다 다를때, 최대 가져갈 수 있는 마리수
    kinds = len(set(nums))
    print(takes) #가져갈 수 있는 마리수
    print(kinds) #폰켓몬 중복제거한 종류
    answer = min(kinds, takes)
    
    return answer