def mean(xs):
    if not xs:
        raise ValueError("mean requires at least one value")
    return sum(xs) / len(xs)
