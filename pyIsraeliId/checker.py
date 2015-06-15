


def validate_israeli_id_number(tz):
    tz = [((lambda i: 2 if i % 2 else 1)(multiplier), int(d)) for multiplier, d in enumerate(str(tz))]
    min_len = 8
    full_len = 9
    given_len = len(tz)

    if given_len < min_len or given_len > full_len:
        return False
    elif given_len == min_len:
        tz.insert(0, (0, 0))  # pad with leading zero

    total = 0
    for multiplier, digit in tz:
        product = multiplier * digit
        total += product if product <= 9 else sum([int(d) for d in str(product)])

    return False if total % 10 else True
