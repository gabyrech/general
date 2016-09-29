#!/usr/bin/python
#http://pypi.python.org/pypi/fisher/
from fisher import pvalue
import sys

infile = open(sys.argv[1]).readlines()

columA = 0
columB = 0

for line in infile[1:]:
    valueA = int(line.split("\t")[1])
    columA += valueA
    valueB = int(line.split("\t")[2])
    columB += valueB

print "Category" + "\t" + "columA_IN" + "\t" + "columB_IN" + "\t" + "columA_OUT" + "\t" + "columB_OUT" + "\t" + "propA" + "\t" + "propB" + "\t" + "p.two_tail" + "\t" + "p.right_tail" + "\t" + "p.left_tail"


for line in infile[1:]:
    cat = line.split("\t")[0]
    columA_IN = int(line.split("\t")[1])
    columB_IN = int(line.split("\t")[2])
    columA_OUT = columA-columA_IN
    columB_OUT = columB-columB_IN
    propA = float(columA_IN/float(columA))
    propB = float(columB_IN/float(columB))
    p = pvalue(columA_IN, columA_OUT, columB_IN, columB_OUT)
    print cat + "\t" + str(columA_IN) + "\t" + str(columB_IN) + "\t" + str(columA_OUT) + "\t" + str(columB_OUT) + "\t" + str(propA) + "\t" + str(propB) + "\t" + str(p.two_tail) + "\t" + str(p.right_tail) + "\t" + str(p.left_tail)
