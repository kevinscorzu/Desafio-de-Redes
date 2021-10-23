import numpy as np
import cv2
import utils

def histogramEqualization(inImageName, outImageName):

    A = cv2.imread(inImageName, cv2.IMREAD_GRAYSCALE)
    
    B = cv2.equalizeHist(A)

    cv2.imwrite(outImageName, B)

    return

def discreteFourierTransform(inImageName, outImageName):

    A = cv2.imread(inImageName, cv2.IMREAD_GRAYSCALE)

    A = np.double(A)
    F = np.fft.fft2(A)

    F = utils.convertComplexImage(np.log(1 + np.abs(F)))

    cv2.imwrite(outImageName, F)

    return

def discreteFourierTransformShift(inImageName, outImageName):

    A = cv2.imread(inImageName, cv2.IMREAD_GRAYSCALE)

    A = np.double(A)
    F = np.fft.fft2(A)

    Fshift = np.fft.fftshift(F)

    Fshift = utils.convertComplexImage(np.log(1 + np.abs(Fshift)))

    cv2.imwrite(outImageName, Fshift)

    return

def lowPassIdealFilter(D0, inImageName, outImageName):

    A = cv2.imread(inImageName, cv2.IMREAD_GRAYSCALE)

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

    cv2.imwrite(outImageName, B)

    return

def highPassIdealFilter(D0, inImageName, outImageName):

    A = cv2.imread(inImageName, cv2.IMREAD_GRAYSCALE)

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

    cv2.imwrite(outImageName, B)

    return 

def lowPassGaussianFilter(sigma, inImageName, outImageName):

    A = cv2.imread(inImageName, cv2.IMREAD_GRAYSCALE)

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

    cv2.imwrite(outImageName, B)

    return

def highPassGaussianFilter(sigma, inImageName, outImageName):

    A = cv2.imread(inImageName, cv2.IMREAD_GRAYSCALE)

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

    cv2.imwrite(outImageName, B)

    return

def lowPassButterworthFilter(D0, n, inImageName, outImageName):

    A = cv2.imread(inImageName, cv2.IMREAD_GRAYSCALE)

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

    cv2.imwrite(outImageName, B)

    return

def highPassButterworthFilter(D0, n, inImageName, outImageName):

    A = cv2.imread(inImageName, cv2.IMREAD_GRAYSCALE)

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

    cv2.imwrite(outImageName, B)

    return