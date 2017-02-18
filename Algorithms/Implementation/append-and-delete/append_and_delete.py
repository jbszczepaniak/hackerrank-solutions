def common_prefix_len(first,second):
    pref_len = 0
    while(first[0] == second[0]):
        pref_len += 1
        first, second = first[1:], second[1:]
        if first == "" or second == "":
            break
    return pref_len

def is_convertable(s,t,steps):
    pref_len = common_prefix_len(s,t)
    diff_without_pref = len(s) + len(t) - 2 * pref_len

    # Parity is the same, we can add and delete one char from threshold
    # set on sum of differing characters.
    if steps % 2 == diff_without_pref % 2:
        if steps >= diff_without_pref:
            return True
        else:
            return False
    # Parity differs, minimal threshold from which we can delete on empty
    # string is set as sum of lengts of both strings.
    else:
        if steps >= len(s) + len(t):
            return True
        else:
            return False
