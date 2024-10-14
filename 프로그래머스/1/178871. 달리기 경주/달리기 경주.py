def solution(players, callings):
    
    dict = {p:i for i,p in enumerate(players)}
    #print(dict)
    
    for c in callings:
        i = dict[c]
        players[i-1], players[i] = players[i], players[i-1]  #>> 시간초과
        #print(c, i, players, dict)
        dict[players[i]] = i
        dict[players[i-1]] = i-1
        
    return players