import unittest
import requests
import utils

baseUrl = "http://40.84.176.73"
baseFrontEndUrl = baseUrl + ":80/"
baseBackEndUrl = baseUrl + ":2727/"

class TestOperations(unittest.TestCase):
    def testFrontEnd(self):
        r = requests.get(baseFrontEndUrl)
        
        self.assertEqual(r.status_code, 200, "Debe ser 200: F")

    def testHistogramEqualization(self):
        inImagePath = "test_images\Sydney.jpeg"
        outImagePath = "test_images\out\SydneyHistogramEqualization.png"

        base64Image = (utils.encodeB64Image(inImagePath)).decode("utf-8")

        r = requests.post(baseBackEndUrl + "histogram-equalization/", json = {"image": base64Image})
        utils.decodeB64Image(r.json()["image"], outImagePath)

        self.assertEqual(r.status_code, 200, "Debe ser 200: BHE")

    def testDiscreteFourierTransform(self):
        inImagePath = "test_images\BabyYoda.jpg"
        outImagePath = "test_images\out\BabyYodaDFT2D.png"

        base64Image = (utils.encodeB64Image(inImagePath)).decode("utf-8")

        r = requests.post(baseBackEndUrl + "discrete-fourier-transform/", json = {"image": base64Image})
        utils.decodeB64Image(r.json()["image"], outImagePath)

        self.assertEqual(r.status_code, 200, "Debe ser 200: BDFT")

    def testDiscreteFourierTransformShift(self):
        inImagePath = "test_images\BabyYoda.jpg"
        outImagePath = "test_images\out\BabyYodaDFT2DS.png"

        base64Image = (utils.encodeB64Image(inImagePath)).decode("utf-8")

        r = requests.post(baseBackEndUrl + "discrete-fourier-transform-shift/", json = {"image": base64Image})
        utils.decodeB64Image(r.json()["image"], outImagePath)

        self.assertEqual(r.status_code, 200, "Debe ser 200: BDFTS")

    def testLowPassIdealFilter(self):
        inImagePath = "test_images\EdificioChina.jpg"
        outImagePath = "test_images\out\EdificioChinaLPIF.png"

        base64Image = (utils.encodeB64Image(inImagePath)).decode("utf-8")

        r = requests.post(baseBackEndUrl + "low-pass-ideal-filter/80/", json = {"image": base64Image})
        utils.decodeB64Image(r.json()["image"], outImagePath)

        self.assertEqual(r.status_code, 200, "Debe ser 200: BLPIF")

    def testHighPassIdealFilter(self):
        inImagePath = "test_images\EdificioChina.jpg"
        outImagePath = "test_images\out\EdificioChinaHPIF.png"

        base64Image = (utils.encodeB64Image(inImagePath)).decode("utf-8")

        r = requests.post(baseBackEndUrl + "high-pass-ideal-filter/80/", json = {"image": base64Image})
        utils.decodeB64Image(r.json()["image"], outImagePath)

        self.assertEqual(r.status_code, 200, "Debe ser 200: BHPIF")

    def testLowPassGaussianFilter(self):
        inImagePath = "test_images\EdificioChina.jpg"
        outImagePath = "test_images\out\EdificioChinaLPGF.png"

        base64Image = (utils.encodeB64Image(inImagePath)).decode("utf-8")

        r = requests.post(baseBackEndUrl + "low-pass-gaussian-filter/80/", json = {"image": base64Image})
        utils.decodeB64Image(r.json()["image"], outImagePath)

        self.assertEqual(r.status_code, 200, "Debe ser 200: BLPGF")

    def testHighPassGaussianFilter(self):
        inImagePath = "test_images\EdificioChina.jpg"
        outImagePath = "test_images\out\EdificioChinaHPGF.png"

        base64Image = (utils.encodeB64Image(inImagePath)).decode("utf-8")

        r = requests.post(baseBackEndUrl + "high-pass-gaussian-filter/80/", json = {"image": base64Image})
        utils.decodeB64Image(r.json()["image"], outImagePath)

        self.assertEqual(r.status_code, 200, "Debe ser 200: BHPGF")

    def testLowPassButterworthFilter(self):
        inImagePath = "test_images\EdificioChina.jpg"
        outImagePath = "test_images\out\EdificioChinaLPBF.png"

        base64Image = (utils.encodeB64Image(inImagePath)).decode("utf-8")

        r = requests.post(baseBackEndUrl + "low-pass-butterworth-filter/80/2/", json = {"image": base64Image})
        utils.decodeB64Image(r.json()["image"], outImagePath)

        self.assertEqual(r.status_code, 200, "Debe ser 200: BLPBF")

    def testHighPassButterworthFilter(self):
        inImagePath = "test_images\EdificioChina.jpg"
        outImagePath = "test_images\out\EdificioChinaHPBF.png"

        base64Image = (utils.encodeB64Image(inImagePath)).decode("utf-8")

        r = requests.post(baseBackEndUrl + "high-pass-butterworth-filter/80/2/", json = {"image": base64Image})
        utils.decodeB64Image(r.json()["image"], outImagePath)

        self.assertEqual(r.status_code, 200, "Debe ser 200: BHPBF")

if __name__ == '__main__':
    unittest.main()