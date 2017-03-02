def min_jumps(clouds):
    jump_cnt = 0
    i = 0
    while i <= len(clouds) - 2 :
        perspective = clouds[i+1:i+3]
        if perspective == [0,1]:
            i += 1
        else:
            i += 2  # It is guaranteed that perspective = [1,0]
        jump_cnt += 1
    return jump_cnt