import unittest
import cv2
import sys
import os
sys.path.insert(0, './')
sys.path.insert(0, '../../')
from utils.HttpMethod import http_post
from utils.Base64 import image_b64, b64_image, b64_feat
from utils.Config import config


pointColor = (0, 0, 255)
pointSize = 2
thickness = -1
retColor = (0, 255, 0)
retSize = 2
testFile = './static/test.jpg'
saveFile = './static/output.jpg'
data = {
    'image': image_b64(cv2.imread(testFile)[:, :, [2, 1, 0]])
}
testUrl = "http://" + config['serverIp'] + ':' + str(config['serverPort']) + '/face-detect'
headers = {
    'Content-Type': 'application/json'
}


class detectTest(unittest.TestCase):
    def testRun(self):
        img = cv2.imread(testFile)
        res = http_post(testUrl, data, headers=headers)
        points = res['points']
        bounding_boxes = res['bounding_boxes']
        for ind, item in enumerate(bounding_boxes):
            item = {key: int(item[key]) for key in item}
            cv2.rectangle(img, (item['x'], item['y']), (item['w'], item['h']), retColor, retSize)
        for ind, item in enumerate(points):
            item = b64_feat(item)
            for i in range(5):
                cv2.circle(img, (item[i], item[i+5]), pointSize, pointColor, thickness)
        cv2.imwrite(saveFile, img)
