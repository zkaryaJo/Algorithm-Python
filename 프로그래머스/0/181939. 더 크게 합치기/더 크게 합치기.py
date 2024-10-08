def solution(a, b):
    str1, str2 = str(a)+str(b), str(b)+str(a)
    answer = int(str1) if int(str1) >= int(str2) else int(str2)
    return answer