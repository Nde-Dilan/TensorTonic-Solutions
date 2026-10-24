import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A=np.asarray(A)
    a,b = A.shape
    A_transpose=np.zeros((b,a))
    i=0
    j=0
    for x in A:
        for y in x:
            A_transpose[i][j] = y
            i+=1
        i=0
        j+=1

    return A_transpose
    
