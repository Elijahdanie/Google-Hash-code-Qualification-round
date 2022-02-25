#!/usr/bin/python3

"""
This module is the entry point for the application
"""

import sys
from filereader import load_Data

with open(sys.argv[1], 'r') as f:
    filecontents = f.readlines()
    fileparsed = [i.split('\n')[0] for i in filecontents]
    cont, proj = map(int, fileparsed[0].split())
    fp = fileparsed[1:]
    pdata = load_Data(cont, proj, fp)
    results = str(proj) + '\n'
    for p in pdata['projects']:
        p.Assign(pdata['contributors'])
        results += p.render() + '\n'
    print(results, end='')
