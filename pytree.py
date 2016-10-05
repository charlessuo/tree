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


def prepare_dir(new_path, counts, the_end, padding):
    counts[0] = counts[0] + 1
    if (the_end):
        padding = padding + padding0
    else:
        padding = padding + paddingI
    print_tree(new_path, counts, padding)
    padding = padding[:-4]


def print_tree(path, counts, padding=""):
    children = prepare_path(path)
    for i in range(0, len(children)):
        the_end = False
        if (i == len(children) - 1):
            the_end = True
            print(padding + paddingL + children[i])
        else:
            print(padding + paddingT + children[i])
        new_path = os.path.join(path, children[i])
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
    print()
    dir_str = "directories"
    file_str = "files"
    print("{} {}, {} {}".format(counts[0], dir_str, counts[1], file_str))
