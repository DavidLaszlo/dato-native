"""
Beating the Benchmark
Truly Native?
__author__ : David Shinn
"""
from __future__ import print_function
import datacreator
import myrandomforestclassifier

import glob
import multiprocessing

import pandas as pd

print('--- Read training labels')
train_labels = pd.read_csv('../../../data/train_v2.csv')
train_keys = dict([a[1] for a in train_labels.iterrows()])
test_files = set(pd.read_csv('../../../data/sampleSubmission_v2.csv').file.values)

file_paths = glob.glob('../../../data/*/*.txt')
num_tasks = len(file_paths)
results = {}
if __name__ == '__main__':
    p = multiprocessing.Pool()
    results = p.map([datacreator.create_data(path, train_keys) for path in file_paths])
    p.close()
    p.join()

print("--- Data read and mapped: {:,}".format(len(results), end=''))
df_full = pd.DataFrame(list(results))

submission = myrandomforestclassifier.classify(pd.DataFrame(list(results)), test_files)
submission.to_csv('../../../native_btb_basic_submission.csv', index=False)