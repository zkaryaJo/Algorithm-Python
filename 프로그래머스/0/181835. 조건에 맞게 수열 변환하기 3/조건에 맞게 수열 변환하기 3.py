def solution(arr, k):
    answer = []
    for n in arr:
        answer.append(n*k if k%2 != 0 else n+k)
    return answer