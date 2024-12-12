def solution(s):
    answer = 0
    
    #1. 스택 사용하기
    
    #2. 모든 경우의수 구하기(길이만큼 회전하기)
    
    for i in range(len(s)):
        if i>0 :
            first = s[:1]
            remain = s[1:]
            s = remain+first
        
        isRightString = True
        
        stack = []
        for j in range(len(s)):
            c = s[j]
            # print(s, answer)
            
            #유효성검사
            if c == ']' or c == '}' or c ==')':
                if not stack:
                    isRightString = False
                    break
                top = stack.pop()
                if c==']' and top !='[':
                    isRightString = False
                    break
                elif c=='}' and top !='{':
                    isRightString = False
                    break
                elif c==')' and top !='(':
                    isRightString = False
                    break
                
            if c == '[' or c == '(' or c == '{' :
                stack.append(s[j])
        
        if isRightString and len(stack) == 0 :
            answer += 1
    
    return answer