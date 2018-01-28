#!/usr/bin/env python3

import os
import sys
import re
import subprocess
from glob import glob

for fn_v in glob('*.webm'):
    fn_a = fn_v.replace('.webm', '.m4a')
    if fn_a in glob('*.m4a'):
        newname = re.sub(r'-.{,11}\.webm', '.mkv', fn_v)
        run = subprocess.run('mkvmerge -o "{}" "{}" "{}"'.format(newname, fn_v, fn_a), shell=True)
        try:
            run.check_returncode()
        except:
            exit()
        else:
            os.remove(fn_a)
            os.remove(fn_v)
