#! bin/python

import json
from binascii import unhexlify
from collections import deque
from shutil import move

def apply(jfile):
  with open(jfile,'r') as j:
    patch = json.load(j)
  if not 'file' in patch:
    print("Error: Invalid patch file given, no file param present")
    return
  outfile = patch['file']+'.tmp'
  with open(patch['file'],'r') as f, open(outfile,'w') as of:
    lineid = 1
    diffs = deque(patch['diff'])
    for rx in iter(lambda: f.readline(),''):
      if str(lineid) not in diffs:
        of.write(rx)
      else:
        of.write(unhexlify(patch[str(lineid)]))
        diffs.popleft()
      lineid = lineid + 1
    for wx in diffs:
      of.write(unhexlify(patch[wx]))
  move(outfile,patch['file'])

if __name__ == "__main__":
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument("jfile", help="Patch JSON file")
  args = parser.parse_args()
  apply(args.jfile)
