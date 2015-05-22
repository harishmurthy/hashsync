#! bin/python

from hashlib import md5
from binascii import hexlify

def text_merkle_tree(infile,content=None):
  with open(infile,'r') as f:
    mer = {}
    lineid = 1
    for x in iter(lambda: f.readline(), ''):
      mer['line'+str(lineid)] = hexlify(md5(x.encode()).digest())
      if content is not None:
        content[str(lineid)] = hexlify(x.encode())
      lineid = lineid + 1
    return mer

if __name__ == "__main__":
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument("file", help="File for which merkle tree is needed")
  args = parser.parse_args()
  content = {}
  print(text_merkle_tree(args.file,content))
  print(content)
