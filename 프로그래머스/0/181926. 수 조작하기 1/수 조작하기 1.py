def solution(n, control):
    
    #a,d는 한쌍으로 0
    #w,s는 한쌍으로 0
    return n+10*(control.count('d')-control.count('a'))+(control.count('w')-control.count('s'))