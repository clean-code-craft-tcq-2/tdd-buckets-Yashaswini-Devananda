import unittest
import chargeRangeReadings

class chargeRangeReadingsTest(unittest.TestCase):
  
  def test(self):
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([], chargeRangeReadings.ADC_12Bit) == "")
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([0], chargeRangeReadings.ADC_12Bit) == "0-0, 1\n")
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([4094], chargeRangeReadings.ADC_12Bit) == "10-10, 1\n")
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([4094,4095], chargeRangeReadings.ADC_12Bit) == "10-10, 1\n")#ignore error readings
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([0,100,200,400,500,1000,1500,2500,3000,3500,4000], chargeRangeReadings.ADC_12Bit) == "0-2, 6\n 4-4, 1\n 6-7, 2\n 9-10, 2\n")
    
    
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([], chargeRangeReadings.ADC_10Bit) == "")
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([0], chargeRangeReadings.ADC_10Bit) == "-15--15, 1\n")
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([511], chargeRangeReadings.ADC_10Bit) == "0-0, 1\n")
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([1022], chargeRangeReadings.ADC_10Bit) == "15-15, 1\n")
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([1022,1023], chargeRangeReadings.ADC_10Bit) == "15-15, 1\n")#ignore error readings
#     self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([0,100,150,300,500,70,1500,700,600,2000,1022], chargeRangeReadings.ADC_10Bit) == "-15--15, 1 \n -13--11, 3 \n -6--6, 1 \n 0-0, 1 \n 3-3, 1 \n 6-6, 1 \n 15-15, 1 \n")

    
if __name__ == '__main__':
  unittest.main()
  
  
  
