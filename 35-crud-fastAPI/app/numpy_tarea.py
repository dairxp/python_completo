import numpy as np

A = np.diag(np.arange(50))

print("Matriz:\n", A)
print("Dimensiones:", A.ndim)
print("Forma:", A.shape)
print("Tamaño:", A.size)
print("Tipo de elemento:", A.dtype)