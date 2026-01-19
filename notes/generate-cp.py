#!/usr/bin/python3
import re

with open('mapping', 'r') as m:
    mapping = m.readlines()

for pp in mapping:
    pair = pp.split()
    if len(pair) >= 2:
        print ("cp L{}.pdf ../../stqam-1261-pdfs/L{}-{}.pdf".format(pair[0], pair[0], pair[1]))
        print ("cp L{}-slides.pdf ../../stqam-1261-pdfs/L{}-slides-{}.pdf".format(pair[0], pair[0], pair[1]))
    
