def solution(phone_book):
    answer = True
    
    #1. 정렬(문자열대로)
    phone_book.sort()
    
    #2. 앞에부터 한번만 비교
    # for i in range(len(phone_book)):
    #     for j in range(i+1, len(phone_book)):
    #         if phone_book[j].startswith(phone_book[i]):
    #             answer = False
    #             break
    #     if answer == False :
    #         break
    
    #2. 
    for p1, p2 in zip(phone_book, phone_book[1:]):
        #print(p1, p2)
        if p2.startswith(p1):
            answer = False
            break
            
    return answer