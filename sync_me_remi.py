"""
sync_me_remi.py checks the folder ~/Projects/remi/paperss for any new document since the last sync
if there is a new file, it pushes that to remi
"""

import os
from glob import glob
from os.path import basename, join, isfile
import json

def any_new_files():
    filename = "./.old_papers.json"
    remi_dir = './paperss'

    # Open the hidden json that holds the info of the last sync
    if filename:
        with open(filename, 'r') as f:
            old_papers = json.load(f)

    # compare last sync with files in the new dir
    current_papers = dict([(f, None) for f in os.listdir(remi_dir)])
    added = [f for f in current_papers if not f in old_papers]

    # if there are new files return the new files and update the list
    if added:
        # print new old papers json
        with open(filename, 'w') as f:
            json.dump(current_papers, f)

    return(added)

def syn_new_files(added):
    for new in added:
        cmd = "./ReMarkableAPI/remarkable.php upload ./paperss/{0} /".format(new)
        os.system(cmd)

def main():
    # check for new files
    os.chdir("/Users/bstavel/Projects/remi")
    added = any_new_files()
    if added: syn_new_files(added)

if __name__ == "__main__":
    main()
