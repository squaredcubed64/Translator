import pathlib
import random
import string
import re
import numpy as np

text_file = "spa.txt"
with open(text_file, encoding='utf-8') as f:
    lines = f.read().split("\n")[:-1]

newLines = []

for line in lines:
    eng = line.split("\t")[0]
    line = eng
    newLines.append(line)

with open("eng.txt", "w") as txt_file:
    for line in newLines:
        txt_file.write(line + "\n")
