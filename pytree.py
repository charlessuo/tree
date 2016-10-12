#!/usr/bin/env python3
import sys
import os
import re
import string


indent = "│   "
indent_end = "    "
branch = "├── "
branch_end = "└── "


def path_tree(curr_dir, padding=""):
    child = []
    temp = os.listdir(curr_dir)
    for t in temp:
        if t[0] != '.':
            child.append(t)
    child.sort()
    #return child
    ndirs = 0
    nfiles = 0
    for i in range(len(child)):
        filename = child[i]
        if i < len(child) - 1:
            print (padding + branch + filename)
        else:
            print (padding + branch_end + filename)
        nfiles += 1
        new_path = os.path.join(curr_dir, filename)
        if os.path.isdir(new_path):
            temp = path_tree(new_path, padding + indent)
        else:
            temp = path_tree(new_path, padding + indent_end)
            ndirs += temp[0]
            nfiles += temp[1]
            ndirs += 1
        return ndirs, nfiles


if __name__ == '__main__':
    if (len(sys.argv) > 2):
        print("Error")
        sys.exit()
    ndirs, nfiles = 0, 0
    curr_dir = "."
    if len(sys.argv) == 2:
        curr_dir = sys.argv[1]
    print(curr_dir)
    temp = path_tree(curr_dir)
    ndirs, nfiles = temp[0], temp[1]
    print()
    print("{} {}, {} {}".format(ndirs, (" directories, " if ndirs != 1 else " directory, "), nfiles, (" files" if nfiles != 1 else " file")))
