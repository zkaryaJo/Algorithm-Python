def solution(n, times):
    answer = 0
    
    # 최소시간 ~ 최대시간 중에서 n을 소화할 수 있는 시간을 찾는다.
        #최소시간 : min(times) * 1
        #최대시간 : max(times) * n
    
    l = min(times)
    r = max(times) * n
    
    while l <= r :
        m = (l + r) // 2
        
        people = 0
        for time in times:
            people += m // time
            
            #다 끝나지도 않았는데 n을 초과하면 의미가 없음.
            if people >= n :
                break
        
        if people >= n:
            answer = m
            r = m-1
        else:
            l = m+1
    
    return answer