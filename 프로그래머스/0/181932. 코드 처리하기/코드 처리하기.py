def solution(code):
    
    answer = ''
    mode = False
    for i in range(0, len(code)):
        if(code[i] == '1') :
            mode = not mode
        else :
            if(mode):
                if(i%2==1):
                    answer += code[i]
            else:
                if(i%2==0):
                    answer += code[i]    
    
    return 'EMPTY' if answer == '' else answer;