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
        #arr = self.BW_filter().copy()
        arr = []
        j = complex(0, 1)
        for i1 in range(0, len(self.array)):
            row = []
            for j1 in range(0, len(self.array[i1])):
                tmp = 0.0
                for i2 in range(0, len(arr)):
                    for j2 in range(0, len(arr[0])):
                        tmp = tmp + (self.array[i2][j2][0] * cmath.exp(-2 * cmath.pi * j * ((i1 * i2 / len(arr)) + (j1 * j2 / len(arr[0])))))
                tmp = tmp / (len(self.array) * len(self.array[0]))
                row.append(tmp)
            arr.append(row)
        res = self.array.copy()
        for i in range(0, len(res)):
            for j in range(0, len(res[i])):
                res[i][j][0] = int(math.sqrt(arr[i][j].real*arr[i][j].real+arr[i][j].imag*arr[i][j].imag))
                res[i][j][1] = res[i][j][0]
                res[i][j][2] = res[i][j][0]

        #                arr[i1][j1][0] = tmp   #int(math.sqrt(tmp.real*tmp.real+tmp.imag*tmp.imag))
#                arr[i1][j1][1] = arr[i1][j1][0]
#                arr[i1][j1][2] = arr[i1][j1][0]
        return arr

    def FUR_unfilter(self):
        arr = self.FUR_filter()
        res = self.array.copy()
        j = complex(0, 1)
        for i1 in range(0, len(arr)):
            for j1 in range(0, len(arr[i1])):
                tmp = 0.0
                for i2 in range(0, len(arr)):
                    for j2 in range(0, len(arr[0])):
                        tmp = tmp + (arr[i2][j2] * cmath.exp(2 * cmath.pi * j * ((i1 * i2 / len(arr)) + (j1 * j2 / len(arr[0])))))
                res[i1][j1][0] = int(math.sqrt(tmp.real*tmp.real+tmp.imag*tmp.imag))
                res[i1][j1][1] = res[i1][j1][0]
                res[i1][j1][2] = res[i1][j1][0]
        return res