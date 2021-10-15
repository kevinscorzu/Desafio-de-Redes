import base64
import numpy as np

# Funcion que decodifica una imagen de base 64
def decodeB64Image(image):
    with open("image.jpg", "wb") as f:
        f.write(base64.b64decode(image))
    
    return

# Funcion que codifica una imagen en base 64
def encodeB64Image():
    with open("image.jpg", "rb") as f:
        b64Str = base64.b64encode(f.read())

    return b64Str

# Funcion que convierte una imagen compleja a real
def convertComplexImage(A):
    Amin = np.min(A)
    Amax = np.max(A)
    return np.uint8(np.dot(np.divide(np.subtract(A, Amin), np.subtract(Amax, Amin)), 255))

# Funcion que calcula la matriz D de una imagen
def DMatrixCalculation(A):
    m, n = A.shape
    D = np.zeros((m ,n))
    for u in range(1, m + 1):
        for v in range(1, n + 1):
            D[u - 1, v - 1] = np.sqrt((u - (m / 2)) ** 2 + (v - (n / 2)) ** 2)

    return D