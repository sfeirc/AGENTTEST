def median(xs):
    s = sorted(xs)
    n = len(s)
    if n == 0:
        raise ValueError("median() arg is an empty sequence")
    if n % 2 == 0:
        return (s[n // 2 - 1] + s[n // 2]) / 2
    return s[n // 2]
