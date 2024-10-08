def solution(ineq, eq, n, m):
    
    return int(eval(str(n) +ineq + eq.replace('!','') + str(m)))
    
    # if(eq == '=') :
    #     if(n == m) :
    #         return 1
    #     else :
    #         if(ineq =='>'):
    #             if(n>m):
    #                 return 1
    #             else:
    #                 return 0
    #         else:
    #             if(n<m):
    #                 return 1
    #             else:
    #                 return 0
    # else:
    #     if(ineq =='>'):
    #         if(n>m):
    #             return 1
    #         else:
    #             return 0
    #     else:
    #         if(n<m):
    #             return 1
    #         else:
    #             return 0
          