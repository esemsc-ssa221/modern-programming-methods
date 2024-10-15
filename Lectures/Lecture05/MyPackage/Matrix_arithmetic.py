import numpy as np
from math import sqrt


class MatrixOperator():
    def __init__(self, matrix1, matrix2):
        self.m1 = matrix1
        self.m2 = matrix2

    def add(self):
        try:
            assert type(self.m1) is np.ndarray and type(self.m2) is np.ndarray
            assert np.size(self.m1) == np.size(self.m2)
            return self.m1 + self.m2
        except AssertionError:
            print("Only numpy arrays of same size allowed")

    def subtract(self):
        try:
            assert type(self.m1) is np.ndarray and type(self.m2) is np.ndarray
            assert np.size(self.m1) == np.size(self.m2)
            return self.m1 - self.m2
        except AssertionError:
            print("Only numpy arrays of same size allowed")

    def element_wise_multiplication(self):
        try:
            assert type(self.m1) is np.ndarray and type(self.m2) is np.ndarray
            assert np.size(self.m1) == np.size(self.m2)
            return self.m1 * self.m2
        except AssertionError:
            print("Only numpy arrays of same size allowed")

    def element_wise_division(self):
        # https://github.com/numpy/numpy/issues/19723
        np.seterr(divide='raise')
        try:
            assert type(self.m1) is np.ndarray and type(self.m2) is np.ndarray
            assert np.size(self.m1) == np.size(self.m2)
            return self.m1 / self.m2
        except FloatingPointError:
            print("Cannot divide by zero")
            return
        except AssertionError:
            print("Only numpy arrays of same size allowed")
            return


class MatrixStatistics():
    def __init__(self, matrix):
        self.m = matrix

    def mean(self):
        try:
            assert type(self.m) is np.ndarray
            return np.mean(self.m)
        except AssertionError:
            print("not a numpy array")

    def median(self):
        try:
            assert type(self.m) is np.ndarray
            return np.median(self.m)
        except AssertionError:
            print("not a numpy array")
    
    def standard_deviation(self):
        try:
            assert type(self.m) is np.ndarray
            return sqrt(np.var(self.m))
        except AssertionError:
            print("not a numpy array")


def Determinant(m1):
    if np.shape(m1)[0] == np.shape(m1)[1]:
        return np.linalg.det(m1)
    else:
        print("not a square matrix")
        return    


def Inverse(m1):
    if np.shape(m1)[0] != np.shape(m1)[1]:
        print("not a square matrix")
        return
    elif Determinant(m1) == 0:
        print("matrix with determinant zero has no inverse")
        return
    else:
        return np.invert(m1)


if __name__ == '__main__':   
    operator = MatrixOperator(np.array([2, 1]), np.array([1, 0]))
    print(operator.element_wise_division())
    print(Inverse(np.array([[2, 1], [1, 0.5]])))
    stats = MatrixStatistics(np.array([[2, 1], [1, 0.5]]))
    print(f'Standard deviation of\n{np.array([[2, 1], [1, 0.5]])}:',
          stats.standard_deviation())
