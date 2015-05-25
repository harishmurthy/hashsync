# hashsync
Utility to sync text files using Hash trees, 100% python

Use case:
This can be used if you want to keep a remote directory in sync with a local directory, like rsync

On remote system:
Initially hashtree.py is run over all the files in the directory. It would create JSON files containing hash tree for each file

On local system:
Any time something changed, run syncup.py <changed file> <remote json file>. This would create JSON patch file which can then be fed to filup.py
On remote system, run filup.py <patch file> to incorporate changes.

Currently the JSON files will have to be manually exchanged between systems. But have plan to include as well.

INSTALL:

Clone the repo:
  git clone https://github.com/harishmurthy/hashsync.git

Install virtualenv if you haven't already, then:
  virtualenv hashsync
  cd hashsync && bin/activate
  pip install -r requirements.txt

