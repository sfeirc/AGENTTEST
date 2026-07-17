def median(xs):
    ys = sorted(xs)
    n = len(ys)
    if n == 0:
        raise ValueError("median() arg is an empty sequence")
    mid = n // 2
    if n % 2 == 1:
        return ys[mid]
    return (ys[mid - 1] + ys[mid]) / 2
