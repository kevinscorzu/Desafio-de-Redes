from flask import Flask, request, jsonify
import os
import utils
import operations as op

app = Flask(__name__)

# Funcion que realiza una ecualizacion de histograma de una imagen
@app.route('/histogram-equalization/', methods = ['POST'])
def histogramEqualizationHandler():
    content = request.json
    utils.decodeB64Image(content["image"], "image.jpg")

    op.histogramEqualization("image.jpg", "image.jpg")

    base64Image = (utils.encodeB64Image("image.jpg")).decode("utf-8")

    os.remove("image.jpg")

    return jsonify({'image': base64Image})

# Funcion que calcula la transformada discreta de fourier de una imagen
@app.route('/discrete-fourier-transform/', methods = ['POST'])
def discreteFourierTransformHandler():
    content = request.json
    utils.decodeB64Image(content["image"], "image.jpg")

    op.discreteFourierTransform("image.jpg", "image.jpg")

    base64Image = (utils.encodeB64Image("image.jpg")).decode("utf-8")

    os.remove("image.jpg")

    return jsonify({'image': base64Image})

# Funcion que calcula el modulo de la transformada discreta de fourier de una imagen
@app.route('/discrete-fourier-transform-shift/', methods = ['POST'])
def discreteFourierTransformShiftHandler():
    content = request.json
    utils.decodeB64Image(content["image"], "image.jpg")

    op.discreteFourierTransformShift("image.jpg", "image.jpg")

    base64Image = (utils.encodeB64Image("image.jpg")).decode("utf-8")

    os.remove("image.jpg")

    return jsonify({'image': base64Image})

# Funcion que aplica un filtro ideal pasa bajas a una imagen
@app.route('/low-pass-ideal-filter/<int:D0>/', methods = ['POST'])
def lowPassIdealFilterHandler(D0):
    content = request.json
    utils.decodeB64Image(content["image"], "image.jpg")

    op.lowPassIdealFilter(D0, "image.jpg", "image.jpg")

    base64Image = (utils.encodeB64Image("image.jpg")).decode("utf-8")

    os.remove("image.jpg")

    return jsonify({'image': base64Image})

# Funcion que aplica un filtro ideal pasa altas a una imagen
@app.route('/high-pass-ideal-filter/<int:D0>/', methods = ['POST'])
def highPassIdealFilterHandler(D0):
    content = request.json
    utils.decodeB64Image(content["image"], "image.jpg")

    op.highPassIdealFilter(D0, "image.jpg", "image.jpg")

    base64Image = (utils.encodeB64Image("image.jpg")).decode("utf-8")

    os.remove("image.jpg")

    return jsonify({'image': base64Image})

# Funcion que aplica un filtro gausiano pasa bajas a una imagen
@app.route('/low-pass-gaussian-filter/<int:sigma>/', methods = ['POST'])
def lowPassGaussianFilterHandler(sigma):
    content = request.json
    utils.decodeB64Image(content["image"], "image.jpg")

    op.lowPassGaussianFilter(sigma, "image.jpg", "image.jpg")

    base64Image = (utils.encodeB64Image("image.jpg")).decode("utf-8")

    os.remove("image.jpg")

    return jsonify({'image': base64Image})

# Funcion que aplica un filtro gausiano pasa altas a una imagen
@app.route('/high-pass-gaussian-filter/<int:sigma>/', methods = ['POST'])
def highPassGaussianFilterHandler(sigma):
    content = request.json
    utils.decodeB64Image(content["image"], "image.jpg")

    op.highPassGaussianFilter(sigma, "image.jpg", "image.jpg")

    base64Image = (utils.encodeB64Image("image.jpg")).decode("utf-8")

    os.remove("image.jpg")

    return jsonify({'image': base64Image})

# Funcion que aplica un filtro butterworth pasa bajas a una imagen
@app.route('/low-pass-butterworth-filter/<int:D0>/<int:n>/', methods = ['POST'])
def lowPassButterworthFilterHandler(D0, n):
    content = request.json
    utils.decodeB64Image(content["image"], "image.jpg")

    op.lowPassButterworthFilter(D0, n, "image.jpg", "image.jpg")

    base64Image = (utils.encodeB64Image("image.jpg")).decode("utf-8")

    os.remove("image.jpg")

    return jsonify({'image': base64Image})

# Funcion que aplica un filtro butterworth pasa altas a una imagen
@app.route('/high-pass-butterworth-filter/<int:D0>/<int:n>/', methods = ['POST'])
def highPassButterworthFilterHandler(D0, n):
    content = request.json
    utils.decodeB64Image(content["image"], "image.jpg")

    op.highPassButterworthFilter(D0, n, "image.jpg", "image.jpg")

    base64Image = (utils.encodeB64Image("image.jpg")).decode("utf-8")

    os.remove("image.jpg")

    return jsonify({'image': base64Image})

# Funcion principal del programa
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 2727)