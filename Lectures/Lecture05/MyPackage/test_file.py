from MyPackage import Matrix_arithmetic
import numpy as np


Matrix1 = np.array([[2, 1], [1, 3]])
Matrix2 = np.array([[1, 3], [2, 6]])
TestOperator = Matrix_arithmetic.MatrixOperator(Matrix1, Matrix2)


def test_add():
    added_array = np.array([[3, 4],[3, 9]])
    assert np.allclose(TestOperator.add(), added_array)
    return

def test_subtract():
    subtracted_array = np.array([[1, 2],[-1, -3]])
    assert np.allclose(TestOperator.subtract(), subtracted_array)
    return

def test_divide():
    divided_array = np.array([[2, 1/3],[0.5, 0.5]])
    assert np.allclose(divided_array, TestOperator.element_wise_division())
    return

def test_multiply():
    multiplied_array = np.array([[2, 3],[2, 8]])
    assert np.allclose(multiplied_array, TestOperator.element_wise_multiplication())
    return

