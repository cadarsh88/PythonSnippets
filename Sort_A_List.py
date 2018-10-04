#Hit compile and run to see a sample output.
#Read values from stdin, do NOT hard code input.

import fileinput
import sys

filelist = []

for line in fileinput.input():
    filelist.append(line.strip())
lengthoflist = filelist[0]
lengthoflistnum = int(lengthoflist)
unsortedlist = filelist[1:]
sortedlist = sorted(unsortedlist, key = lambda s:s.lower())
print("\n".join(sortedlist))