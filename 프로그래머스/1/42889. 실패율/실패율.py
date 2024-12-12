from collections import Counter

def solution(N, stages):
    
    #1. 현재 스테이지별 도전자수 구하기
    challenger = [0]*(N+2)
    for stage in stages:
        challenger[stage] += 1
    
    #print(challenger)
    
    #2. 스테이지별 실패자수 구하기
    fails = {}
    total = len(stages)

    #3. 각 스테이지 순회하며, 실패율계산
    for i in range(1, N+1):
        if challenger[i] == 0:
            fails[i] = 0
        else:
            fails[i] = challenger[i] / total
            total -= challenger[i]
    
    #print(fails)
    
    #실패율이 높은 스테이지부터 정렬
    result = sorted(fails, key=lambda x : fails[x], reverse=True)
    
    
    
    #4. 
    
#     #1. 행렬만들기 (-1로 모두 초기화)
#     row, col = N, len(stages)
#     answer = []
#     arr = list([-1]*col for _ in range(row))
    
#     #2. 행렬에 값 채우기
#     #행렬로 계산
#     #r1 : 0 1 0 0 0 0 0 0
#     #r2 : 1 - 1 0 1 0 0 0
#     #r3 : - - - 0 - 0 1 1
#     #r4 : - - - 0 - 0 - -
#     #r5 : - - - 0 - 0 - -
#     #r6 : - - - 0 - 1 - -
#     for i in range(row):
#         for j in range(col):
#             if i+1 < stages[j] : 
#                 arr[i][j] = 0
#             elif i+1 == stages[j] : 
#                 arr[i][j] = 1
#             else :
#                 arr[i][j] = -1
            
#     #3. -1, 0, 1의 갯수 각각 세기
#     count_list = list(Counter(row) for row in arr)
    
#     #4. 실패인원 / 도전자수 : 1(실패) / 0(성공)+1(실패)
#     # [{0.125: 1}, 
#     # {0.42857142857142855: 2}, 
#     # {0.5: 3}, 
#     # {0.5: 4}, 
#     # {0.0: 5}]
#     fail_list = list({cRow[1]/(cRow[0]+cRow[1]) : i+1 } for i, cRow in enumerate(count_list))
        
#     sorted_fail_list = sorted(fail_list, key=lambda x: list(x.keys())[0], reverse=True)
    
#     # [{0.5: 3},
#     #  {0.5: 4}, 
#     #  {0.42857142857142855: 2}, 
#     #  {0.125: 1}, 
#     #  {0.0: 5}]
#     print(sorted_fail_list)
    
#     answer = [list(item.values())[0] for item in sorted_fail_list]
    
    return result
