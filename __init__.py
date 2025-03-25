import os
from cudatext import *

class Command:
    def __init__(self):
        return

    def test(self):
        dir_test = os.path.join(os.path.dirname(os.path.realpath(__file__)), '_test')
        file_open(os.path.join(dir_test, 'test.py'))
        #
        ed.bookmark(BOOKMARK_SET, 3)
        #
        imagelist_proc(ed.decor(DECOR_GET_IMAGELIST), IMAGELIST_ADD, os.path.join(dir_test, 'test.png'))
        ed.decor(DECOR_SET, line=6, image=0)
        #
        ed.bookmark(BOOKMARK_SET, 9)
        ed.decor(DECOR_SET, line=9, image=0)