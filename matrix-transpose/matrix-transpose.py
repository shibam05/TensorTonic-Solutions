import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here

    T = [[j for j in range(len(A))] for i in range(len(A[0]))]

    for i in range(len(A)):
        for j in range(len(A[0])):
            T[j][i] = A[i][j]
    
    return np.array(T)

    # or,
    # A = np.matrix(A)
    # return np.transpose(A)

    
