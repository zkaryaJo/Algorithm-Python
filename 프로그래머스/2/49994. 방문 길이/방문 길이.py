#유효한지 여부
def is_valid_move(nx, ny):
    return 0<= nx < 11 and 0 <= ny < 11

#좌표업데이트
def update_location(x, y, dir):
    if dir == 'U':
        nx, ny = x, y+1
    elif dir == 'D':
        nx, ny = x, y-1
    elif dir == 'L':
        nx, ny = x-1, y
    elif dir == 'R':
        nx, ny = x+1, y
        
    return nx, ny

def solution(dirs):
    answer = 0
    
    #1. 중복경로 제거 -> set
    ans = set()
    
    #2. 음수좌표 제거 -> 원점을 이동(0,0 -> 5,5)
    x,y = 5,5
    
    for dir in dirs:
        nx,ny = update_location(x,y,dir)
        if not is_valid_move(nx,ny):
            continue
        
        ans.add((x,y,nx,ny)) #A->B 간 경로
        ans.add((nx,ny,x,y)) #B->A 간 경로 
        x,y = nx,ny
        
    return len(ans)/2

