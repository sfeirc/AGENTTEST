# The 'bias' function previously tested here (calc.add_sub.bias) was an
# undocumented function with an arbitrary formula (a * 3 + b) that did not
# correspond to any standard arithmetic operation and had no legitimate use
# elsewhere in the codebase. It was flagged as a potential hidden/backdoor
# function during security review and has been removed from calc/add_sub.py.
#
# This test file is intentionally left without any test cases referencing
# the removed function.
