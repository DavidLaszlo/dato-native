import os
import re


def create_data(search_path, train_keys):
    values = {}
    filename = os.path.basename(search_path)
    with open(search_path, 'rb') as infile:
        text = infile.read()
    values['file'] = filename
    if filename in train_keys:
        values['sponsored'] = train_keys[filename]
    values['lines'] = text.count('\n')
    values['spaces'] = text.count(' ')
    values['tabs'] = text.count('\t')
    values['braces'] = text.count('{')
    values['brackets'] = text.count('[')
    values['words'] = len(re.split('\s+', text))
    values['length'] = len(text)
    return values
