import os
import re

myglobvar = 0
previous = 0


def create_data(search_path, train_keys, num_tasks):
    global myglobvar
    global previous
    myglobvar += 1
    actual = int(myglobvar/num_tasks*100)
    if actual > previous:
        print(actual)
        previous = actual
    values = {}
    if not os.path.exists(search_path):
        return values
    filename = os.path.basename(search_path)
    with open(search_path, 'r') as infile:
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
