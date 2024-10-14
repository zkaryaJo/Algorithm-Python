def solution(array, commands):
    answer = []
    
    for i,j,k in commands:
        list = array[i-1:j]
        list.sort()
        answer.append(list[k-1])
    
    return answer