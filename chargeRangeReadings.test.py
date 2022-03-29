import unittest
import chargeRangeReadings

class chargeRangeReadingsTest(unittest.TestCase):
  
  def test(self):
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([], chargeRangeReadings.ADC_12Bit) == "")
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([], chargeRangeReadings.ADC_10Bit) == "")
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([4094], chargeRangeReadings.ADC_12Bit) == "10-10, 1\n")
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([0], chargeRangeReadings.ADC_12Bit) == "0-0, 1\n")
    
if __name__ == '__main__':
  unittest.main()
  
  
  
