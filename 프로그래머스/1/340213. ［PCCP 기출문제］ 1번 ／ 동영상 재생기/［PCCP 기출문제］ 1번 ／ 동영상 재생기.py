def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    #분/초를 초단위로 통일
    op_start_sec = int(op_start.split(":")[0])*60+int(op_start.split(":")[1])
    op_end_sec = int(op_end.split(":")[0])*60+int(op_end.split(":")[1])
    
    pos_sec = int(pos.split(":")[0])*60+int(pos.split(":")[1])
    video_sec = int(video_len.split(":")[0])*60+int(video_len.split(":")[1])
    
    for cmd in commands:
        if pos_sec >= op_start_sec and pos_sec <= op_end_sec:
            #print(pos_sec, op_end_sec)
            pos_sec = op_end_sec
        
        if "next" == cmd :
            pos_sec += 10
        else:
            pos_sec -= 10
            
        if pos_sec < 0 : 
            pos_sec = 0
        
        if pos_sec > video_sec:
            pos_sec = video_sec
    
    #마지막으로 수행한 코드가 오프닝시간에 있으면, 오프닝 마지막시간으로 변경
    if pos_sec >= op_start_sec and pos_sec <= op_end_sec:
        pos_sec = op_end_sec
    
    #print(pos_sec, int(pos_sec/60), pos_sec%60)
    
    #포멧팅, :02는 없을때 0을 붙이는 두자리수 포멧팅 방법!
    answer = f"{int(pos_sec/60):02}:{pos_sec%60:02}"
    return answer