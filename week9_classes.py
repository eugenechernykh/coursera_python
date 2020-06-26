'''
This is the final code for the week #9
'''
from copy import deepcopy
from sys import stdin

class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    # The static method mustn't change the original matrix
    @staticmethod
    def transposed(m):
        m_transponed = [map(lambda j: m.matrix[j][i], range(len(m.matrix))) for
                        i in range(len(m.matrix[0]))]
        return Matrix(m_transponed)

    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def transpose(self):
        # The method must change the original matrix
        m = self.matrix
        m_transponed = [map(lambda j: m[j][i], range(len(m))) for
                        i in range(len(m[0]))]
        self.matrix = m_transponed
        return Matrix(self.matrix)

    def __str__(self):
        my_str = ''
        for item in self.matrix:
            my_str += '\t'.join(map(str, item)) + '\n'
        return my_str[:-1]

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, other):
        m = self.matrix
        k = other.matrix
        if len(m) != len(k) or len(m[0]) != len(k[0]):
            error = MatrixError(self, other)
            raise error
        else:
            summa = [map(lambda a, b: a + b, m[i], k[i]) for i in
                     range(len(m))]
        return Matrix(summa)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Matrix(
                [map(lambda x: x * other, item) for item in self.matrix])

    __rmul__ = __mul__


m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 1, 0]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)
print(m1 * 10)
print(m1.transpose())

# exec(stdin.read())
