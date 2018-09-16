#!/usr/bin/env python
"""mapper.py"""

import sys
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

r1 = re.compile(r"[^a-zA-Z .]+")
r2 = re.compile(r"[\.]")

top_words = ['game','warriors','said','james','cavaliers','team','points','games','first','durant']

stop_words = set(stopwords.words('english'))
p = PorterStemmer()

filtered_words =[]
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().lower()
    line = r1.sub("",line)
    line = r2.sub(" ",line)
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1

        if (word in stop_words):
            continue
        filtered_words.append(word)

        
    for word in filtered_words:
        if(word in top_words):
                for word2 in filtered_words:
                    if(word2!=word and word2 in top_words):
                        pair = [word,word2]
                        print '%s\t%s' % (pair, 1)
