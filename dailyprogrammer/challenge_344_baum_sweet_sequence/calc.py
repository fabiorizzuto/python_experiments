def calculate_b(n):
    zero_seq = 0
    while True:
        rest = n % 2
        if rest == 0:
            zero_seq += 1
        else:
            if zero_seq % 2 == 1:
                return 0
        n //= 2
        if n == 0:
            break
    return 1
