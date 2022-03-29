import unittest
import chargeRangeReadings

class chargeRangeReadingsTest(unittest.TestCase):
  
  def test(self):

    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([6,4,5]) == " 4-6, 3 \n")
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([1,1,1,1,1,1,1]) == " 1-1, 7 \n")
    self.assertTrue(chargeRangeReadings.getFreqOfChargeRanges([5,6,10,11,12,14,16,17,21,25,24,26]) == " 5-6, 2 \n 10-12, 3 \n 14-14, 1 \n 16-17, 2 \n 21-21, 1 \n 24-26, 3 \n" )
    print (chargeRangeReadings.getFreqOfChargeRanges([5,6,10,11,12,14,16,17,21,25,24,26]))

# __name__ == '__main__':
unittest.main()
  
  
  
