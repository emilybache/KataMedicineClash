import unittest
from datetime import date, timedelta
from prescription import Prescription

class PrescriptionTest(unittest.TestCase):
    
    def test_completion_date(self):
        prescription = Prescription(dispense_date = date.today() - timedelta(days=15), days_supply = 30)
        self.assertEquals(date.today() + timedelta(days=15), prescription.completion_date())
        
    def test_days_supply(self):
        prescription = Prescription(dispense_date = date.today(), days_supply = 3)
        self.assertEquals([date.today(), date.today()+timedelta(days=1), date.today()+timedelta(days=2)], prescription.days_taken())
        
        
if __name__ == "__main__":
    unittest.main()