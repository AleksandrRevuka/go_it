import sys


def parse_args():
    result = " ".join([arg for arg in sys.argv[1:]])
    return result


print(parse_args())
#   python modul_4/task_14.py first second
