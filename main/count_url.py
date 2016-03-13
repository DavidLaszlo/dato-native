"""

Beating the Benchmark
Truly Native?
__author__ : David Shinn

"""
from __future__ import print_function

from collections import Counter
import glob
import multiprocessing
import os
import re
import sys
import time

from sklearn.ensemble import RandomForestClassifier
import pandas as pd


def split(text):
# http://superuser.com/questions/623168/regex-to-parse-urls-from-text
# http://daringfireball.net/2010/07/improved_regex_for_matching_urls

	urls = re.findall('(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?]))', text)
	urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
	print(urls)
	return urls
	
def create_data(filepath):
    values = {}
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as infile:
        text = infile.read()
    values['file'] = filename
 #   if filename in train_keys:
 #       values['sponsored'] = train_keys[filename]
    values['lines'] = text.count('\n')
    values['spaces'] = text.count(' ')
    values['tabs'] = text.count('\t')
    values['braces'] = text.count('{')
    values['brackets'] = text.count('[')
    values['words'] = len(re.split('\s+', text))
    values['length'] = len(text)
    values['urls'] = len(split(text))
    return values

filepaths = glob.glob('./raw_html.txt');
results = map(create_data, filepaths)

print(results);
