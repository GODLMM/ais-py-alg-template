import unittest
import os


rootSrc = './test/'

#get currect dirName that include testCase
filesName = [rootSrc + path for path in os.listdir(rootSrc) if not path.startswith('_')]
dirs = [path for path in filesName if os.path.isdir(path)]
# initializer the testSuite
suite = unittest.TestSuite()
#add testCase into suite
for dirname in dirs:
    dirCases = unittest.defaultTestLoader.discover(dirname, 'test*.py', top_level_dir=dirname)
    for case in dirCases:
        suite.addTest(case)
# begin the testRunner
runner = unittest.TextTestRunner()
runner.run(suite)