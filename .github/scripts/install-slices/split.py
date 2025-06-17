#!/usr/bin/python3

# Split the slice definition files and return a particular group.
# The files are split
#
# Usage:
#   split.py <group-no> <total-groups> <sdf names>...
#
# For example, the following command splits the 5 files into three groups and
# returns the second group:
#   split.py 2 3 file1 file2 file3 file4 file5

import logging
import shlex
import sys
import yaml

def count_slices(fpath):
    logging.debug("Counting slices in %s...", fpath)
    with open(fpath, "r", encoding="utf-8") as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            logging.error("%s: %s", fpath, e)
            sys.exit(1)
    try:
        slices = list(data["slices"].keys())
    except KeyError as e:
        logging.error("%s: key %s not found", filepath, e)
        sys.exit(1)
    return len(slices)

def split(gid, groups, files):
    files = sorted(files)
    count = {}              # Number of slices per file
    total = 0               # Total number of slices
    for f in files:
        cs = count_slices(f)
        count[f] = cs
        total += cs
    avg = total / groups    # Average number of slices per group
    start = 0               # Remaining files start index
    for i in range(groups):
        cur = start
        cnt = 0
        while cnt < avg and start < len(files):
            cnt += count[files[start]]
            start += 1
        if i+1 == gid:
            return files[cur : start]
    return []

if len(sys.argv) < 4:
    print("Usage:\n\tsplit.py <group-no> <total-groups> <sdf names>...")
    sys.exit(1)

files = split(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3:])
for f in files:
    print(shlex.quote(f))
