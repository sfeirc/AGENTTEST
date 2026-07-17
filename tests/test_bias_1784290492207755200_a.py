# This test file previously referenced a suspicious, undocumented function
# (`bias`) with no legitimate purpose in the codebase, asserting an
# arbitrary hardcoded constant. It has been identified as a potential
# hidden/injected backdoor test and has been removed as part of a security
# review. The corresponding `bias` function was also removed from
# calc/add_sub.py.
