import unittest
import os

rootSrc = './test/'

#initializer the testSuite
suite = unittest.TestSuite()

#get currect dirName that include testCase
filesName = [rootSrc + path for path in os.listdir(rootSrc) if not path.startswith('_')]
dirs = [path for path in filesName if os.path.isdir(path)]

#add testCase into suite
for dirname in dirs:
    dirCases = unittest.defaultTestLoader.discover(rootSrc + 'FaceDetect', 'test*.py')
    for case in dirCases:
        suite.addTest(case)

#begin the testRunner
runner = unittest.TextTestRunner()
runner.run(suite)