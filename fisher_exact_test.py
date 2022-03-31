#!/usr/bin/python
#http://pypi.python.org/pypi/fisher/
from fisher import pvalue
import sys

#Usage:
#  there is any difference of property in selected vs. non-selected groups?
# python fisher_exact_test.py 12 5 29 2
#				Having the property		Not having the property
#Selected			12				5
#Not selected			29				2

p = pvalue(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
#print p.left_tail, p.right_tail, p.two_tail
#print "Two Tail p: " + str(p.two_tail)
#print "Right Tail p: " + str(p.right_tail)
#print "Left Tail p: " + str(p.left_tail)

print str(sys.argv[1]) + "\t" + str(sys.argv[2]) + "\t" + str(sys.argv[3]) + "\t" + str(sys.argv[4]) + "\t" + \
    "TwoTail-p:" + str(p.two_tail) + "\t" + "RightTail-p:" + str(p.right_tail) + "\t" + "Left-Tail-p:" + str(p.left_tail)
