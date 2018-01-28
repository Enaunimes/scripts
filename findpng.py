#!/usr/bin/env python3
from glob import glob
from PIL import Image

for imgfile in glob('**.jpg',recursive=True):
    img = Image.open(imgfile)
    if img.format == 'PNG':
        print(imgfile)

