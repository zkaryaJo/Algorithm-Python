def solution(numbers, target):
    answer = 0
    
    #BFS 풀이
    #입출력예시2
    #i=0일때 leaves = [4, -4]
    #i=1일때 leaves = [5,3, -3,-5]
    #i=2일때 leaves = [7,3,5,1, -1,-5,-3,-7]
    #i=3일때 leaves = [8,6,4,2,6,4,2,0,...]
    
    leaves = [0]
    
    for i, num in enumerate(numbers):
        tmp = []
        for parent in leaves:
            tmp.append(parent+num)
            tmp.append(parent-num)
        leaves = tmp
    
    for i in leaves:
        if i == target:
            answer = answer+1
    
    return answer