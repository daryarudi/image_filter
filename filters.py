import math
import cmath
import numpy as np


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

    def IDL_filter(self, w, d0):
        arr = self.FUR_filter()
        arr_new = arr.copy()
        matrix = []
        for i in range(0, len(arr)):
            row = []
            for j in range(0, len(arr[0])):
                tmp = math.sqrt((i - len(arr) / 2) ** 2 + (j - len(arr[0]) / 2) ** 2)
                if (tmp < d0) or (tmp > (d0 + w)):
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        for i in range(0, len(arr)):
            for j in range(0, len(arr[0])):
                arr_new[i][j] = arr[i][j] * matrix[i][j]
        return self.FUR_unfilter(arr_new)

    def shift(self, arr):
        arr_new = []
        for i in range(0, len(arr)):
            row = []
            for j in range(0, len(arr[0])):
                row.append(arr[i][j] * ((-1) ** (i + j)))
            arr_new.append(row)
        return arr_new

    def pix_to_float(self, arr):
        arr_new = []
        for i in range(0, len(arr)):
            row = []
            for j in range(0, len(arr[0])):
                row.append(float(self.array[i][j][0]))
            arr_new.append(row)
        return arr_new

    def float_to_pix(self, arr):
        arr_new = self.array.copy()
        for i in range(0, len(arr)):
            for j in range(0, len(arr[0])):
                value = int(math.sqrt(arr[i][j].real**2+arr[i][j].imag**2))#int(arr[i][j].real)#
                if (value > 255):
                    value = 255
                arr_new[i][j][0] = value
                arr_new[i][j][1] = arr_new[i][j][0]
                arr_new[i][j][2] = arr_new[i][j][0]
        return arr_new

    def FUR_filter(self):
        self.array = self.BW_filter()
        n = len(self.array)
        m = len(self.array[0])

        arr0 = self.pix_to_float(self.array)
        arr0 = self.shift(arr0)

        arr1 = []
        for i in range(0, n):
            arr1.append([])
        for i in range(0, n):
            for j in range(0, m):
                tmp = 0.0
                for k in range(0, m):
                    tmp = tmp + arr0[i][k] * (math.cos((2 * math.pi * j * k) / m) + 1j * math.sin((2 * math.pi * j * k) / m))
                arr1[i].append(tmp)
        arr2 = []
        for i in range(0, n):
            arr2.append([])
        for i in range(0, m):
            for j in range(0, n):
                tmp = 0.0
                for k in range(0, n):
                    tmp = tmp + arr1[k][i] * (math.cos((2 * math.pi * j * k) / m) + 1j * math.sin((2 * math.pi * j * k) / m))
                arr2[j].append(tmp)
#        res = self.float_to_pix(arr2)
        return arr2

    def FUR_unfilter(self, arr0):
        n = len(arr0)
        m = len(arr0[0])
        arr1 = []
        for i in range(0, n):
                arr1.append([])
        for i in range(0, n):
            for j in range(0, m):
                tmp = 0.0
                for k in range(0, m):
                    tmp = tmp + arr0[i][k] * (math.cos((2 * math.pi * j * k) / m) - 1j * math.sin((2 * math.pi * j * k) / m))
                arr1[i].append(tmp/m)
        arr2 = []
        for i in range(0, n):
            arr2.append([])
        for i in range(0, m):
            for j in range(0, n):
                tmp = 0.0
                for k in range(0, n):
                    tmp = tmp + arr1[k][i] * (math.cos((2 * math.pi * j * k) / m) - 1j * math.sin((2 * math.pi * j * k) / m))
                arr2[j].append(tmp/n)
        arr2 = self.shift(arr2)
        res = self.float_to_pix(arr2)
        return res