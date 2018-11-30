import numpy
import copy


def gauss(a, B):
    eps = 1e-16

    a = numpy.append(a, B.reshape((-1, 1)), axis=1)

    len1 = len(a[:, 0])
    len2 = len(a[0, :])

    def forward():
        for g in range(len1):
            max = abs(a[g][g])
            my = g
            t1 = g
            while t1 < len1:
                if abs(a[t1][g]) > max:
                    max = abs(a[t1][g])
                    my = t1
                t1 += 1

            if abs(max) < eps:
                raise DetermExeption("Check determinant")

            if my != g:
                b = copy.deepcopy(a[g])
                a[g] = copy.deepcopy(a[my])
                a[my] = copy.deepcopy(b)

            amain = float(a[g][g])

            z = g
            while z < len2:
                a[g][z] = a[g][z] / amain
                z += 1
            j = g + 1

            while j < len1:
                b = a[j][g]
                z = g
                while z < len2:
                    a[j][z] = a[j][z] - a[g][z] * b
                    z += 1
                j += 1

    def backward():
        i = len1 - 1
        while i > 0:
            j = i - 1
            while j >= 0:
                a[j][len1] = a[j][len1] - a[j][i] * a[i][len1]
                j -= 1
            i -= 1
        return a[:, len2 - 1]

    forward()
    return backward()


class DetermExeption(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


a = numpy.array([
    [1, 2, 1],
    [3, 2, 3],
    [1, 0, 0]
], dtype=float)

b = numpy.array([5, 6, 7], dtype=float)

print(gauss(a, b))
