#!/usr/bin/env python3
import sys
import os
import re
import string


paddingI = "│   "
padding0 = "    "
paddingT = "├── "
paddingL = "└── "


def prepare_path(path):
    child = []
    temp = os.listdir(path)
    for t in temp:
        if t[0] != '.':
            child.append(t)
    child.sort()
    return child


def print_tree(path, counts, padding=""):
    children = prepare_path(path)
    for i in range(0, len(children)):
        the_end = False
        if (os.path.isdir(new_path)):
            prepare_dir(new_path, counts, the_end, padding)
        else:
            counts[1] = counts[1] + 1


if __name__ == '__main__':
    if (len(sys.argv) > 2):
        print("Invalid")
        sys.exit()
    counts = [0, 0]
    path = "."
    if len(sys.argv) == 2:
        path = sys.argv[1]
    print(path)
    print_tree(path, counts)
