def solution(arr, queries):

    #swap 가능
    for i,j in queries:
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr
