#!/usr/bin/python3

import os
import json

arches, releases = json.loads(os.environ["ARCHES"]), json.loads(os.environ["RELEASES"])
splits = int(json.loads(os.environ["SPLITS"]))
if splits < 2:
    splits = 1
matrix = []
for arch in arches:
    for release in releases:
        for chisel_version in release["chisel-versions"]:
            for i in range(splits):
                matrix.append({
                    "arch": arch,
                    "ref": release["ref"],
                    "chisel-version": chisel_version,
                    "id": i+1,
                })

print(json.dumps(matrix))
