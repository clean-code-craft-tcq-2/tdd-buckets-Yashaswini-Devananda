import unittest
import chargeRangeReadings

class chargeRangeReadingsTest(unittest.TestCase):
  
  def test(self):
#     response = chargeRangeReadings.getFreqOfChargeRanges([6,4,5])
#     print(response)
#     self.assertTrue(response == " 4-6, 3 \n")

    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([6,4,5]) == " 4-6, 3 \n")
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([1,1,1,1,1,1,1) == " 1-1, 7 \n")


if __name__ == '__main__':
  unittest.main()
  
  
  
