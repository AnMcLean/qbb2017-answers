#!/usr/bin/env python

"""
Usage: ./04-Man-automater
"""

import os

for i in range(1, 47):
    os.system("./03-Manhattan-plot.py " + "gwas_output.P" + str(i) + ".assoc.linear")