from PIL import (Image)
import numpy as np
from PySide2.QtGui import (QPixmap)
import datetime
from datetime import datetime
from variables import variables
from filters import filters
from __main__ import *


class image:
    def __init__(self, way):
        self.way = way
        self.dir = way[:way.rindex("/") + 1]

    def to_rgb_array(self):
        self.im = Image.open(self.way)
        img_copy = self.im.copy()
        return np.asarray(img_copy, dtype='uint8')

    def array_to_image(self, arr):
        im = Image.fromarray(arr)
        way = self.dir + self.unique_name()
        im.save(way)
        return image(way)

    def unique_name(self):
        name = str(datetime.now().timestamp())
        name = name[:10] + name[11:] + ".jpg"
        return name

    def to_qpixmap(self):
        return QPixmap(self.way)

    def filter(self, filter_name):
        self.f = filters(self.to_rgb_array())
        if (filter_name == "INF"):
            new_arr = self.f.INF_filter(w = 10, d0 = 30)
        if (filter_name == "IVF"):
            new_arr = self.f.IVF_filter(w = 10, d0 = 30)
        if (filter_name == "BNF"):
            new_arr = self.f.BNF_filter(n = 1, d0 = 30)
        if (filter_name == "BVF"):
            new_arr = self.f.BVF_filter(n = 1, d0 = 30)
        if (filter_name == "GNF"):
            new_arr = self.f.GNF_filter(d0 = 30)
        if (filter_name == "GVF"):
            new_arr = self.f.GVF_filter(d0 = 30)
        return self.array_to_image(new_arr)
