def balancedStringSplit(self, s: str) -> int:
    l_count = 0 
    r_count = 0
    count = 0
    for c in s:
        if c == 'L':
            l_count += 1
        else:
            r_count += 1
        if l_count == r_count:
            count += 1

    return count