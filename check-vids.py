#!/Users/tonyflorida/.pyenv/shims/python
# Create structure for new video project

import os
import mac_tag
from pathlib import Path

tag = "Upload"
root_dir = Path('/Volumes/vid/')
upload = mac_tag.find([tag])

count = 0
warn = 0
for up in upload:
    count = count + 1
    child = Path(up)
    if not root_dir in child.parents:
        warn += 1
        print('WARNING: Path {} not in {}'.format(child, root_dir))
        continue
    num_drp = len(list(child.glob('*.drp')))
    if num_drp != 1:
        warn += 1
        print('WARNING: Found {} drp files in {}'.format(num_drp, child))
    num_png = len([i for i in list(child.glob('*.png')) if not str(i).startswith('.')])
    if num_png < 1:
        warn += 1
        print('WARNING: Found {} png files in {}'.format(num_png, child))

if warn == 0 and count > 0:
    print('All "{}" videos have a .drp and .png files'.format(tag))
else:
    print('Problem(s) found')