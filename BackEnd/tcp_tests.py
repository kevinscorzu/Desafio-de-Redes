import unittest
import socket

baseIp = "40.84.176.73"

class TestOperations(unittest.TestCase):
    def testFrontEnd(self):
        fsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        location = (baseIp, 80)
        result = fsocket.connect_ex(location)

        fsocket.close()
        
        self.assertEqual(result, 0, "El puerto 80 no esta abierto: F")

    def testBackEnd(self):
        bsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        location = (baseIp, 2727)
        result = bsocket.connect_ex(location)

        bsocket.close()
        
        self.assertEqual(result, 0, "El puerto 2727 no esta abierto: F")

if __name__ == '__main__':
    unittest.main()