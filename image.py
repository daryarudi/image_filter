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
        filter = filters(self.to_rgb_array())
        if (filter_name == "BW"):
            new_arr = filter.BW_filter()
        if (filter_name == "NEG"):
            new_arr = filter.NEG_filter()
        if (filter_name == "FUR"):
            new_arr = filter.FUR_unfilter()
        return self.array_to_image(new_arr)
