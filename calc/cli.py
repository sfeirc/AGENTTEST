import sys

from calc.add_sub import add, sub
from calc.mul_div import div, mul

OPS = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
}


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    ops = "|".join(OPS)
    if len(argv) != 3 or argv[0] not in OPS:
        print(f"usage: cli.py <{ops}> <a> <b>")
        return 2
    op = argv[0]
    try:
        a, b = float(argv[1]), float(argv[2])
    except ValueError:
        print("error: <a> and <b> must be numbers")
        return 2
    try:
        print(OPS[op](a, b))
    except ZeroDivisionError:
        print("error: division by zero")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
