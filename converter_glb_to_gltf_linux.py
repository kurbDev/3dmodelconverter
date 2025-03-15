import os
import sys

import glob
import trimesh

def substring_between(s, delim1, delim2):
    return s.partition(delim1)[2].partition(delim2)[0]

def converter(sourcefolder, targetfolder):
    outputdir = f"{targetfolder}"
    os.makedirs(outputdir, exist_ok=True)

    files = glob.glob(f"{sourcefolder}/*.{sourcefolder}")

    for file in files:
        print(file)
        object = trimesh.load(file)

        filename = substring_between(file, "/", ".")
        print(filename)

        object.export(f"{targetfolder}/{filename}.{targetfolder}")


converter(sys.argv[1], sys.argv[2])