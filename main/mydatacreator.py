import os
import re

def create_data(filepath):
    values = {}
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as infile:
        text = infile.read()
    values['file'] = filename
    if filename in train_keys:
        values['sponsored'] = train_keys[filename]
    else:
	values['sponsored'] = NULL;
    values['lines'] = text.count('\n')
    values['spaces'] = text.count(' ')
    values['tabs'] = text.count('\t')
    values['braces'] = text.count('{')
    values['brackets'] = text.count('[')
    values['words'] = len(re.split('\s+', text))
    values['length'] = len(text)
    return values

