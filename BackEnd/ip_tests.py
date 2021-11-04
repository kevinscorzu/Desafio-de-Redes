import unittest
import os

ip = "40.84.176.73"

class TestOperations(unittest.TestCase):
    def testAzureVirtualMachine(self):
        response = os.popen(f"ping {ip}").read()
        success = 0

        if "Received = 4" in response:
            success = 1
        
        self.assertEqual(success, 1, "No fue posible identificar la ip")

if __name__ == '__main__':
    unittest.main()