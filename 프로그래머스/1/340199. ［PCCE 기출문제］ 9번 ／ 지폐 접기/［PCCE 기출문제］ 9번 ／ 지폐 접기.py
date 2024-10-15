def solution(wallet, bill):
    answer = 0
    
    wallet_min = min(wallet[0], wallet[1])
    wallet_max = max(wallet[0], wallet[1])
    
    while(wallet_min < min(bill[0], bill[1]) or 
          wallet_max < max(bill[0], bill[1])):
        if bill[0] > bill[1] :
            bill[0] = bill[0]//2
        else:
            bill[1] = bill[1]//2
        answer += 1
    
    return answer