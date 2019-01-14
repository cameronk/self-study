def solution(num):
    orders    = [(1, 'I'), (10, 'X'), (100, 'C'), (1000, 'M'), (10000, '??')]
    midpoints = [(5, 'V'), (50, 'L'), (500, 'D'), (5000, '?')]
    
    def spread(lower, upper, pos):
        if pos <= 3:
            return lower[1]*pos
        else:
            return lower[1]*(5-pos) + upper[1]

    def digit(i, oom):
        if oom > 2:
            pos = int(i/orders[3][0])
            return "M"*pos

        lower, mid, upper = orders[oom], midpoints[oom], orders[oom+1]
        pos = int(i/lower[0])
        
        if pos <= 3:
            return lower[1]*pos
        elif pos < 5:
            return lower[1]*(5-pos) + mid[1]
        elif pos <= 8:
            return mid[1] + lower[1]*(pos-5)
        else:
            return lower[1]*(pos-8) + upper[1]
      
    
    num_str = str(num)
    N = len(num_str)
    ooms = [(int(n)*10**(N-i-1), N-i-1) for i, n in enumerate(num_str)]
    return ''.join([digit(*x) for x in ooms])
    
    
print(solution(1989))