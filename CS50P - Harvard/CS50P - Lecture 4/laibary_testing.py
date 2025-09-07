import sys

from sayings import goodbye


if len(sys.argv) > 1:
    goodbye(sys.argv[1])