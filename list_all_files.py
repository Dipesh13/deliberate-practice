# You can use glob:

import glob, os

os.chdir("/mydir")
for file in glob.glob("*.txt"):
    print(file)

# or simply os.listdir:

import os

for file in os.listdir("/mydir"):
    if file.endswith(".txt"):
        print(os.path.join("/mydir", file))

# or if you want to traverse directory, use os.walk:

import os

for root, dirs, files in os.walk("/mydir"):
    for file in files:
        if file.endswith(".txt"):