"""
Beating the Benchmark
Truly Native?
__author__ : David Shinn
"""

from __future__ import print_function
import mydatacreator
import myrandomforestclassifier
import glob
import multiprocessing
import time
import sys
import datetime
import pandas as pd


def print_time():
    ts = time.time();
    st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    print(st)


print('Hello')

print_time()
print('--- Read training labels')
train_labels = pd.read_csv('../../../data/train_v2.csv')
train_keys = dict([a[1] for a in train_labels.iterrows()])

num_tasks = len(train_labels)
print('Train labels found: ')
print(num_tasks)
file_paths = glob.glob('../../../data/*/*/*.txt')

p = multiprocessing.Pool()
results = p.map(mydatacreator.create_data, file_paths)
#while (True):
#    completed = results._index
#    print("\r--- Completed {:,} out of {:,}".format(completed, num_tasks), end='')
#    sys.stdout.flush()
#    time.sleep(1)
#    if (completed == num_tasks): break
p.close()
p.join()

print("--- Data read and mapped: {:,}".format(len(results), end=''))

test_files = set(pd.read_csv('../../../data/sampleSubmission_v2.csv').file.values)
submission = myrandomforestclassifier.classify(pd.DataFrame(list(results)), test_files)
submission.to_csv('../../../my_native_btb_basic_submission.csv', index=False)
print_time()
