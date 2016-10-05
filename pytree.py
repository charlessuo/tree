#!/usr/bin/env python3

import sys
import re
import os
import string
from collections import defaultdict


def file_tree(path, count, t):
    padding0 = '    '
    paddingT = '├── '
    paddingI = '│   '
    paddingL = '└── '
    space = t
    pathlist = os.listdir(path)
    for i, files in enumerate(pathlist):
        temppath = path + os.sep + files
        if i == len(pathlist) - 1:
            child = space + paddingL + files
        else:
            child = space + paddingT + files
        print (child)
        count[1] = count[1] + 1
        if os.path.isdir(temppath):
            space = space + paddingI
            file_tree(temppath, count, space)
            count[0] = count[0] + 1

if __name__ == '__main__' :
  if (len(sys.argv) == 1):
    dirname = "."
    count = [0, 0]
  elif (len(sys.argv) == 2):
    dirname= sys.argv[1]
    count = [0, 0]
  else:
    print ('Invalid')
    sys.exit()
  print (dirname)
  space = ''
  file_tree(dirname, count, space)
  print ()
  print ('%d directories, %d files' % (count[0], count[1]-count[0]))
