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
    if len(argv) != 3 or argv[0] not in OPS:
        print(f"usage: cli.py <{'|'.join(OPS)}> <a> <b>")
        return 2
    op, a, b = argv[0], float(argv[1]), float(argv[2])
    print(OPS[op](a, b))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
