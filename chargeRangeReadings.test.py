import unittest
import chargeRangeReadings

class chargeRangeReadingsTest(unittest.TestCase):
  
  def test(self):
    response = chargeRangeReadings.getFreqOfChargeRanges([6,4,5])
    print(response)
    self.assertTrue(response == "4-6, 3")
      


if __name__ == '__main__':
  unittest.main()
  
  
  
