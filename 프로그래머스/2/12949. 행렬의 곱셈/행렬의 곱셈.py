def solution(arr1, arr2):
    
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])
    
    print(f'r1:{r1}, c1:{c1}')
    print(f'r2:{r2}, c2:{c2}')
    
    #2. answer 초기화
    answer = [[0]*c2 for _ in range(r1)]
    
    #3. arr1의 각 행과, arr2의 각 열에 대해
    for i in range(r1) : #
        for j in range(c2):
            for k in range(c1):
                answer[i][j] += arr1[i][k] * arr2[k][j]
            # print(answer[i][j])
    
    print(answer)
    
    return answer