import unittest
import lib as lib
import json

class TestLevelOneMethods(unittest.TestCase):

    def testCleanSample(self):
        self.assertEqual(lib.cleanStringWithSample("sample#load_avg_1m"), "load_avg_1m")

    def testConvertStringToDict(self):
        input = "id=0060cd38-9dd5-4eff-a72f-9705f3dd25d9 service_name=api process=api.233 sample#load_avg_1m=0.849 sample#load_avg_5m=0.561 sample#load_avg_15m=0.202"
        desiredOutput = {"id":"0060cd38-9dd5-4eff-a72f-9705f3dd25d9","service_name":"api","process":"api.233","load_avg_1m":"0.849","load_avg_5m":"0.561","load_avg_15m":"0.202"}
        output = lib.convertStringToDict(input)
        self.assertEqual(desiredOutput,output)

if __name__ == '__main__':
    unittest.main()