def solution(wallpaper):
    answer = []

    #1. 제일 큰 값들로 초기화
    lux, luy, rdx, rdy = 50, 50, 0, 0
    
    for i, line in enumerate(wallpaper):
        #print(i, line)
        for j, c in enumerate(line):
            if c != '#':
                continue
            #print(i,j)
            if i<lux : 
                lux = i
            if i>rdx : 
                rdx = i
            if j<luy : 
                luy = j
            if j > rdy :
                rdy = j
    
    answer = [lux, luy, rdx+1, rdy+1]
    
    return answer