def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        
        #쿼리 하나씩 계산.
        min_val = 1000001
        for n in arr[s:e+1]:
            if (n > k):
                min_val = min(n, min_val)
        
        #num이 안바뀐경우 : -1 인 경우
        answer.append(-1 if min_val == 1000001 else min_val)
                
    return answer