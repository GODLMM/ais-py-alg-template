import unittest
import cv2
import sys
sys.path.insert(0, './')
sys.path.insert(0, '../../')


from utils.HttpMethod import http_post
from utils.Base64 import image_b64
from utils.Config import config

testFile = './static/test.jpg'
data = {
    'image': image_b64(cv2.imread(testFile)[:, :, [2, 1, 0]])
}
test_url = "http://" + config['serverIp'] + ':' + str(config['serverPort']) + '/face-detect'
headers = {
    'Content-Type': 'application/json'
}

class detectTest(unittest.TestCase):
    def testRun(self):
        res = http_post(test_url, data, headers = headers)