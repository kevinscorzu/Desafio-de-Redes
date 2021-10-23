import unittest
import numpy as np
import cv2
import operations as op
import utils

class TestOperations(unittest.TestCase):
    def testHistogramEqualization(self):
        inImagePath = "test_images\Sydney.jpeg"
        outImagePath = "test_images\out\SydneyHistogramEqualization.png"
        expetedImagePath = "test_images\SydneyHistogramEqualization.png"

        op.histogramEqualization(inImagePath, outImagePath)

        base64OutImage = (utils.encodeB64Image(outImagePath)).decode("utf-8")
        base64ExpectedImage = (utils.encodeB64Image(expetedImagePath)).decode("utf-8")

        self.assertEqual(base64OutImage, base64ExpectedImage, "Ambas imagenes deben ser iguales: HE")

    def testDiscreteFourierTransform(self):
        inImagePath = "test_images\BabyYoda.jpg"
        outImagePath = "test_images\out\BabyYodaDFT2D.png"
        expetedImagePath = "test_images\BabyYodaDFT2D.png"

        op.discreteFourierTransform(inImagePath, outImagePath)
        
        base64OutImage = (utils.encodeB64Image(outImagePath)).decode("utf-8")
        base64ExpectedImage = (utils.encodeB64Image(expetedImagePath)).decode("utf-8")

        self.assertEqual(base64OutImage, base64ExpectedImage, "Ambas imagenes deben ser iguales: DFT")

    def testDiscreteFourierTransformShift(self):
        inImagePath = "test_images\BabyYoda.jpg"
        outImagePath = "test_images\out\BabyYodaDFT2DS.png"
        expetedImagePath = "test_images\BabyYodaDFT2DS.png"

        op.discreteFourierTransformShift(inImagePath, outImagePath)
        
        base64OutImage = (utils.encodeB64Image(outImagePath)).decode("utf-8")
        base64ExpectedImage = (utils.encodeB64Image(expetedImagePath)).decode("utf-8")

        self.assertEqual(base64OutImage, base64ExpectedImage, "Ambas imagenes deben ser iguales: DFTS")

    def testLowPassIdealFilter(self):
        inImagePath = "test_images\EdificioChina.jpg"
        outImagePath = "test_images\out\EdificioChinaLPIF.png"
        expetedImagePath = "test_images\EdificioChinaLPIF.png"

        op.lowPassIdealFilter(80, inImagePath, outImagePath)
        
        base64OutImage = (utils.encodeB64Image(outImagePath)).decode("utf-8")
        base64ExpectedImage = (utils.encodeB64Image(expetedImagePath)).decode("utf-8")

        self.assertEqual(base64OutImage, base64ExpectedImage, "Ambas imagenes deben ser iguales: LPIF")

    def testHighPassIdealFilter(self):
        inImagePath = "test_images\EdificioChina.jpg"
        outImagePath = "test_images\out\EdificioChinaHPIF.png"
        expetedImagePath = "test_images\EdificioChinaHPIF.png"

        op.highPassIdealFilter(80, inImagePath, outImagePath)
        
        base64OutImage = (utils.encodeB64Image(outImagePath)).decode("utf-8")
        base64ExpectedImage = (utils.encodeB64Image(expetedImagePath)).decode("utf-8")

        self.assertEqual(base64OutImage, base64ExpectedImage, "Ambas imagenes deben ser iguales: HPIF")

    def testLowPassGaussianFilter(self):
        inImagePath = "test_images\EdificioChina.jpg"
        outImagePath = "test_images\out\EdificioChinaLPGF.png"
        expetedImagePath = "test_images\EdificioChinaLPGF.png"

        op.lowPassGaussianFilter(80, inImagePath, outImagePath)
        
        base64OutImage = (utils.encodeB64Image(outImagePath)).decode("utf-8")
        base64ExpectedImage = (utils.encodeB64Image(expetedImagePath)).decode("utf-8")

        self.assertEqual(base64OutImage, base64ExpectedImage, "Ambas imagenes deben ser iguales: LPGF")

    def testHighPassGaussianFilter(self):
        inImagePath = "test_images\EdificioChina.jpg"
        outImagePath = "test_images\out\EdificioChinaHPGF.png"
        expetedImagePath = "test_images\EdificioChinaHPGF.png"

        op.highPassGaussianFilter(80, inImagePath, outImagePath)
        
        base64OutImage = (utils.encodeB64Image(outImagePath)).decode("utf-8")
        base64ExpectedImage = (utils.encodeB64Image(expetedImagePath)).decode("utf-8")

        self.assertEqual(base64OutImage, base64ExpectedImage, "Ambas imagenes deben ser iguales: HPGF")

    def testLowPassButterworthFilter(self):
        inImagePath = "test_images\EdificioChina.jpg"
        outImagePath = "test_images\out\EdificioChinaLPBF.png"
        expetedImagePath = "test_images\EdificioChinaLPBF.png"

        op.lowPassButterworthFilter(80, 2, inImagePath, outImagePath)
        
        base64OutImage = (utils.encodeB64Image(outImagePath)).decode("utf-8")
        base64ExpectedImage = (utils.encodeB64Image(expetedImagePath)).decode("utf-8")

        self.assertEqual(base64OutImage, base64ExpectedImage, "Ambas imagenes deben ser iguales: LPBF")

    def testHighPassButterworthFilter(self):
        inImagePath = "test_images\EdificioChina.jpg"
        outImagePath = "test_images\out\EdificioChinaHPBF.png"
        expetedImagePath = "test_images\EdificioChinaHPBF.png"

        op.highPassButterworthFilter(80, 2, inImagePath, outImagePath)
        
        base64OutImage = (utils.encodeB64Image(outImagePath)).decode("utf-8")
        base64ExpectedImage = (utils.encodeB64Image(expetedImagePath)).decode("utf-8")

        self.assertEqual(base64OutImage, base64ExpectedImage, "Ambas imagenes deben ser iguales: HPBF")

if __name__ == '__main__':
    unittest.main()