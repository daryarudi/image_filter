import math
import cmath
import numpy as np


class filters:
    def __init__(self, array):
        self.array = array
        self.fur_arr = self.fur()

# идеальный фильтр низкочастотный
    def INF_filter(self, w, d0):
        matrix = []
        for i in range(0, len(self.fur_arr)):
            row = []
            for j in range(0, len(self.fur_arr[0])):
                tmp = self.D(i,j)
                if (tmp < d0) or (tmp > (d0 + w)):
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        return self.un_fur(self.filter(matrix))

# идеальный фильтр высокочастотный
    def IVF_filter(self, w, d0):
        matrix = []
        for i in range(0, len(self.fur_arr)):
            row = []
            for j in range(0, len(self.fur_arr[0])):
                tmp = self.D(i,j)
                if (tmp < d0) or (tmp > (d0 + w)):
                    row.append(0)
                else:
                    row.append(1)
            matrix.append(row)
        return self.un_fur(self.filter(matrix))

# фильтр Баттерворта низкочастотный
    def BNF_filter(self, n, d0):
        matrix = []
        for i in range(0, len(self.fur_arr)):
            row = []
            for j in range(0, len(self.fur_arr[0])):
                row.append(1 / (1 + (self.D(i,j) / d0)**(2 * n)))
            matrix.append(row)
        return self.un_fur(self.filter(matrix))

# фильтр Баттерворта высокочастотный
    def BVF_filter(self, n, d0):
        matrix = []
        for i in range(0, len(self.fur_arr)):
            row = []
            for j in range(0, len(self.fur_arr[0])):
                d = self.D(i,j)
                if (d == 0):
                    row.append(0)
                else:
                    row.append(1 / (1 + (d0 / d)**(2 * n)))
            matrix.append(row)
        return self.un_fur(self.filter(matrix))

# фильтр Гаусса низкочастотный
    def GNF_filter(self, d0):
        matrix = []
        for i in range(0, len(self.fur_arr)):
            row = []
            for j in range(0, len(self.fur_arr[0])):
                row.append(math.exp((-1 * self.D(i, j) ** 2) / (2 * d0 ** 2)))
            matrix.append(row)
        return self.un_fur(self.filter(matrix))

# фильтр Гаусса высокочастотный
    def GVF_filter(self, d0):
        matrix = []
        for i in range(0, len(self.fur_arr)):
            row = []
            for j in range(0, len(self.fur_arr[0])):
                row.append(1 - math.exp((-1 * self.D(i, j) ** 2) / (2 * d0 ** 2)))
            matrix.append(row)
        return self.un_fur(self.filter(matrix))

# вспомогательные методы
    def D(self, u, v):
        return math.sqrt((u - len(self.fur_arr) / 2) ** 2 + (v - len(self.fur_arr[0]) / 2) ** 2)

    def filter(self, matrix):
        arr_new = self.fur_arr.copy()
        for i in range(0, len(self.fur_arr)):
            for j in range(0, len(self.fur_arr[0])):
                arr_new[i][j] = self.fur_arr[i][j] * matrix[i][j]
        return arr_new

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
                if (value < 0):
                    value = 0
                arr_new[i][j][0] = value
                arr_new[i][j][1] = arr_new[i][j][0]
                arr_new[i][j][2] = arr_new[i][j][0]
        return arr_new

    def fur(self):
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

    def un_fur(self, arr0):
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