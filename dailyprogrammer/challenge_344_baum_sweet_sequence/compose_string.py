from calc import calculate_b


def compose_string(nr):
    seq = []
    for i in range(nr + 1):
        seq.append(str(calculate_b(i)))
    return ', '.join(seq)