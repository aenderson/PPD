import json
from subprocess import Popen, CREATE_NEW_CONSOLE
import argparse

def split_indexes(a, n):
  k, m = divmod(len(a), n)
  splitted_data = list((a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in list(range(n))))
  count = 0
  indexes = []
  for split in splitted_data:
      indexes.append(str(count) + '-' + str(len(split)+count-1))
      count += len(split)

  # output will be like: ["0-99", "100-199", "200-299", ...]
  return indexes

# input for the number of workers you choose
parser = argparse.ArgumentParser()
parser.add_argument("--num_workers", type=int, help='Number of workers that will scrape data', default=1)
parsarg = vars(parser.parse_args())

numWorkers = parsarg.get('num_workers')

# load data source!
with open('links.json', 'r') as links:
    data = json.load(links)
# print(data)

# get the array of indexes
# e.g: [“0-99”, “100-199”, “200-299”, ...]
indexes = split_indexes(data['Links'], numWorkers)
# print(indexes)

# for each string in our indexes list, 
# we open a new console that will launch the worker process

for index in indexes:
    Popen(('py worker.py ' + index), creationflags=CREATE_NEW_CONSOLE)
#     # print(index)

