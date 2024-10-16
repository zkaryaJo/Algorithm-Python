def solution(cards1, cards2, goal):
    answer = ''
    
    idx1 = 0
    len1 = len(cards1)
    idx2 = 0
    len2 = len(cards2)
    
    
    for item in goal : 
        if idx1 < len1 and item == cards1[idx1] :
            idx1 += 1
        elif idx2 < len2 and item == cards2[idx2] :
            idx2 += 1
        else :
            return "No"
    
    return "Yes"