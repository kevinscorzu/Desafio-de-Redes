from flask import Flask, request, jsonify
import numpy as np
import cv2
import os
import utils

app = Flask(__name__)

# Funcion que realiza una ecualizacion de histograma de una imagen
@app.route('/histogram-equalization/', methods = ['POST'])
def histogramEqualization():
    content = request.json
    utils.decodeB64Image(content["image"])

    A = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
    
    B = cv2.equalizeHist(A)

    cv2.imwrite("image.jpg", B)

    base64Image = (utils.encodeB64Image()).decode("utf-8")

    os.remove("image.jpg")

    return jsonify({'image': base64Image})

# Funcion que calcula la transformada discreta de fourier de una imagen
@app.route('/discrete-fourier-transform/', methods = ['POST'])
def discreteFourierTransform():
    content = request.json
    utils.decodeB64Image(content["image"])

    A = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

    A = np.double(A)
    F = np.fft.fft2(A)

    F = utils.convertComplexImage(np.log(1 + np.abs(F)))

    cv2.imwrite("image.jpg", F)

    base64Image = (utils.encodeB64Image()).decode("utf-8")

    os.remove("image.jpg")

    return jsonify({'image': base64Image})

# Funcion que calcula el modulo de la transformada discreta de fourier de una imagen
@app.route('/discrete-fourier-transform-shift/', methods = ['POST'])
def discreteFourierTransformShift():
    content = request.json
    utils.decodeB64Image(content["image"])

    A = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

    A = np.double(A)
    F = np.fft.fft2(A)

    Fshift = np.fft.fftshift(F)

    Fshift = utils.convertComplexImage(np.log(1 + np.abs(Fshift)))

    cv2.imwrite("image.jpg", Fshift)

    base64Image = (utils.encodeB64Image()).decode("utf-8")

    os.remove("image.jpg")

    return jsonify({'image': base64Image})

# Funcion que aplica un filtro ideal pasa bajas a una imagen
@app.route('/low-pass-ideal-filter/<int:D0>/', methods = ['POST'])
def lowPassIdealFilter(D0):
    content = request.json
    utils.decodeB64Image(content["image"])

    A = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

    A = np.double(A)
    F = np.fft.fft2(A)

    Fshift = np.fft.fftshift(F)

    D = utils.DMatrixCalculation(A)

    Fmask = np.less_equal(D, D0)

    Fmask = np.fft.fftshift(Fmask)

    Fresult = np.fft.fftshift(np.multiply(F, Fmask))

    Fresult = np.fft.fftshift(Fresult)

    B = np.fft.ifft2(Fresult)
    B = np.uint8(np.abs(B))

    cv2.imwrite("image.jpg", B)

    base64Image = (utils.encodeB64Image()).decode("utf-8")

    os.remove("image.jpg")

    return jsonify({'image': base64Image})

# Funcion que aplica un filtro ideal pasa altas a una imagen
@app.route('/high-pass-ideal-filter/<int:D0>/', methods = ['POST'])
def highPassIdealFilter(D0):
    content = request.json
    utils.decodeB64Image(content["image"])

    A = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

    A = np.double(A)
    F = np.fft.fft2(A)

    Fshift = np.fft.fftshift(F)

    D = utils.DMatrixCalculation(A)

    Fmask = np.greater(D, D0)

    Fmask = np.fft.fftshift(Fmask)

    Fresult = np.fft.fftshift(np.multiply(F, Fmask))

    Fresult = np.fft.fftshift(Fresult)

    B = np.fft.ifft2(Fresult)
    B = np.uint8(np.abs(B))

    cv2.imwrite("image.jpg", B)

    base64Image = (utils.encodeB64Image()).decode("utf-8")

    os.remove("image.jpg")

    return jsonify({'image': base64Image})

# Funcion que aplica un filtro gausiano pasa bajas a una imagen
@app.route('/low-pass-gaussian-filter/<int:sigma>/', methods = ['POST'])
def lowPassGaussianFilter(sigma):
    content = request.json
    utils.decodeB64Image(content["image"])

    A = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

    A = np.double(A)
    F = np.fft.fft2(A)

    Fshift = np.fft.fftshift(F)

    D = utils.DMatrixCalculation(A)

    Fmask = np.exp(np.divide(np.dot(np.power(D, 2), -1), 2 * (sigma ** 2)))

    Fmask = np.fft.fftshift(Fmask)

    Fresult = np.fft.fftshift(np.multiply(F, Fmask))

    Fresult = np.fft.fftshift(Fresult)

    B = np.fft.ifft2(Fresult)
    B = np.uint8(np.abs(B))

    cv2.imwrite("image.jpg", B)

    base64Image = (utils.encodeB64Image()).decode("utf-8")

    os.remove("image.jpg")

    return jsonify({'image': base64Image})

# Funcion que aplica un filtro gausiano pasa altas a una imagen
@app.route('/high-pass-gaussian-filter/<int:sigma>/', methods = ['POST'])
def highPassGaussianFilter(sigma):
    content = request.json
    utils.decodeB64Image(content["image"])

    A = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

    A = np.double(A)
    F = np.fft.fft2(A)

    Fshift = np.fft.fftshift(F)

    D = utils.DMatrixCalculation(A)

    Fmask = np.subtract(1, np.exp(np.divide(np.dot(np.power(D, 2), -1), 2 * (sigma ** 2))))

    Fmask = np.fft.fftshift(Fmask)

    Fresult = np.fft.fftshift(np.multiply(F, Fmask))

    Fresult = np.fft.fftshift(Fresult)

    B = np.fft.ifft2(Fresult)
    B = np.uint8(np.abs(B))

    cv2.imwrite("image.jpg", B)

    base64Image = (utils.encodeB64Image()).decode("utf-8")

    os.remove("image.jpg")

    return jsonify({'image': base64Image})

# Funcion que aplica un filtro butterworth pasa bajas a una imagen
@app.route('/low-pass-butterworth-filter/<int:D0>/<int:n>/', methods = ['POST'])
def lowPassButterworthFilter(D0, n):
    content = request.json
    utils.decodeB64Image(content["image"])

    A = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

    A = np.double(A)
    F = np.fft.fft2(A)

    Fshift = np.fft.fftshift(F)

    D = utils.DMatrixCalculation(A)

    Fmask = np.divide(1, np.add(1, np.power(np.divide(D, D0), 2 * n)))

    Fmask = np.fft.fftshift(Fmask)

    Fresult = np.fft.fftshift(np.multiply(F, Fmask))

    Fresult = np.fft.fftshift(Fresult)

    B = np.fft.ifft2(Fresult)
    B = np.uint8(np.abs(B))

    cv2.imwrite("image.jpg", B)

    base64Image = (utils.encodeB64Image()).decode("utf-8")

    os.remove("image.jpg")

    return jsonify({'image': base64Image})

# Funcion que aplica un filtro butterworth pasa altas a una imagen
@app.route('/high-pass-butterworth-filter/<int:D0>/<int:n>/', methods = ['POST'])
def highPassButterworthFilter(D0, n):
    content = request.json
    utils.decodeB64Image(content["image"])

    A = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

    A = np.double(A)
    F = np.fft.fft2(A)

    Fshift = np.fft.fftshift(F)

    D = utils.DMatrixCalculation(A)

    Fmask = np.divide(1, np.add(1, np.power(np.divide(D0, D), 2 * n)))

    Fmask = np.fft.fftshift(Fmask)

    Fresult = np.fft.fftshift(np.multiply(F, Fmask))

    Fresult = np.fft.fftshift(Fresult)

    B = np.fft.ifft2(Fresult)
    B = np.uint8(np.abs(B))

    cv2.imwrite("image.jpg", B)

    base64Image = (utils.encodeB64Image()).decode("utf-8")

    os.remove("image.jpg")

    return jsonify({'image': base64Image})

# Funcion principal del programa
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 2727)