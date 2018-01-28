#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
from glob import glob

for fn in glob('*'):
    if re.match(r"^.*-[^\s]{,11}\.(mp4|webm)$", fn):
        newname = re.sub(r'-[^\s]{,11}(?=\.(mp4|webm))', '', fn)
        os.rename(fn, newname)
        print('{}\n{}\n'.format(fn,newname))
