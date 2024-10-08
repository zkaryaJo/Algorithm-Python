import numpy

def solution(a, d, included):
    arr = list(range(a, a+len(included)*d, d)) #a 값부터 시작해서 d 만큼 등차수열인 배열을 생성
    return sum([x*int(y) for x,y in zip(arr,included)]) #만들어진 배열과 true, false 배열을 곱셈 한 후 합계출력