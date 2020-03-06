import math
import cmath
import numpy


class filters:
    def __init__(self, array):
        self.array = array

    def BW_filter(self):
        arr = self.array.copy()
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                gray = 0.3 * arr[i][j][0] + 0.59 * arr[i][j][1] + 0.11 * arr[i][j][2]
                arr[i][j][0] = gray
                arr[i][j][1] = gray
                arr[i][j][2] = gray
        return arr

    def NEG_filter(self):
        arr = self.array.copy()
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                arr[i][j][0] = 255 - arr[i][j][0]
                arr[i][j][1] = 255 - arr[i][j][1]
                arr[i][j][2] = 255 - arr[i][j][2]
        return arr

    def FUR_filter(self):
       # numpy.pp
        arr = self.BW_filter().copy()
        j = complex(0, 1)
        for i1 in range(len(arr)):
            for j1 in range(len(arr[i1])):
                tmp1 = 0.0
                for i2 in range(len(arr[0])):
                    tmp2 = 0.0
                    for j2 in range(len(arr)):
                        tmp2 = tmp2 + (self.array[j2][i2][0] * cmath.exp(-2 * cmath.pi * j * j2 * j1 / len(arr[0]))) / len(arr[0])
                    tmp1 = tmp1 + (tmp2 * cmath.exp(-2 * cmath.pi * j * i2 * i1 / len(arr)))/len(arr)
                arr[i1][j1][0] = int(tmp1.real)
                arr[i1][j1][1] = arr[i1][j1][0]
                arr[i1][j1][2] = arr[i1][j1][0]
        return arr