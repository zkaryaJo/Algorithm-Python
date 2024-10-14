from collections import Counter

def solution(participant, completion):
    answer = ''
    
#     첫번째 풀이(각각 정렬 후 같지 않은 항목 바로 반환)
#     participant.sort()
#     completion.sort()
    
#     for p,c in zip(participant, completion):
#         if p != c :
#             return p
        
#     return participant[-1]
    
    # 두번째 풀이(Counter)
    # print(Counter(participant) - Counter(completion))
    # print(Counter(participant) - Counter(completion))
    answer = list(Counter(participant) - Counter(completion))[0]
            
    return answer