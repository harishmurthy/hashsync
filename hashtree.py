#! bin/python

from binascii import unhexlify,hexlify
from collections import deque
from hashlib import md5

class TreeNode:
  def __init__(self,left=None,right=None,chunkid=None,digest=None):
    self.left = left
    self.right= right
    self.chunkid = chunkid
    self.digest = digest

  def comparewith(self,other,l):
    if self.left:
      if other.left:
        if self.left.digest != other.left.digest:
          self.left.comparewith(other.left,l)
      else:
        self.left.getchunks(l)
    if self.right:
      if other.right:
        if self.right.digest != other.right.digest:
          self.right.comparewith(other.right,l)
      else:
        self.right.getchunks(l)
    if self.left is None:
      if self.right is None:
        if other:
          if self.digest != other.digest:
            self.getchunks(l)
        else:
          self.getchunks(l)

  def getchunks(self,l):
    if self.left:
      self.left.getchunks(l)
    if self.right:
      self.right.getchunks(l)
    if self.chunkid:
      l.append(self.chunkid)

  def printtree(self):
    if self.left:
      self.left.printtree()
    if self.right:
      self.right.printtree()
    if self.chunkid:
      print('chunk: ' + str(self.chunkid) + ' -> ' + hexlify(self.digest))

def buildtree(leafdict):
  ml = deque()
  for x in leafdict:
    ml.append(TreeNode(chunkid=x,digest=unhexlify(leafdict[x])))
  if len(ml) % 2:
    t = ml.popleft()
    ml.append(TreeNode(right=t,digest=t.digest,chunkid=[t.chunkid]))
  while len(ml) > 1:
    l = ml.popleft()
    r = ml.popleft()
    ml.append(TreeNode(left=l,right=r,chunkid=[l.chunkid,r.chunkid],digest=md5(l.digest + r.digest).digest()))
  return ml.pop()

if __name__ == "__main__":
  import argparse
  import merkle
  import json
  import binascii
  parser = argparse.ArgumentParser()
  parser.add_argument("file", help="File for which hash tree is needed")
  args = parser.parse_args()
  ld = merkle.text_merkle_tree(args.file)
  mt = buildtree(ld)
  ld['topdigest'] = binascii.hexlify(mt.digest)
  ofile = args.file + '.json'
  with open(ofile,'w') as f:
    json.dump(ld,f,indent=1)
