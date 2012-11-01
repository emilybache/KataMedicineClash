import unittest

from datetime import date, timedelta
from mockito import *

from prescription import Prescription
from medicine import *

class MedicineTest(unittest.TestCase):
    
    def setUp(self):
        self.medicine = Medicine("Aspirin")
    
    def test_possession_end_date(self):
        self.medicine.add_prescription(Prescription(dispense_date = date(2009, 12, 1), days_supply = 30))
        self.assertEquals(date(2009, 12, 31), self.medicine.possession_end_date())
        
    def test_possession_effective_end_date_when_before_today(self):
        self.medicine.add_prescription(Prescription(dispense_date = date.today() - timedelta(days=40), days_supply = 30))
        self.assertEquals(date.today() - timedelta(days=10), self.medicine.possession_effective_end_date())

    def test_possession_effective_end_date_when_after_today(self):
        self.medicine.add_prescription(Prescription(dispense_date = date.today() - timedelta(days=15), days_supply = 30))
        self.assertEquals(date.today(), self.medicine.possession_effective_end_date())
        
    def test_initial_dispense_date(self):
        self.medicine.add_prescription(Prescription(dispense_date = date(2009, 11, 1), days_supply = 30))
        self.medicine.add_prescription(Prescription(dispense_date = date(2009, 11, 30), days_supply = 30))
        self.assertEquals(date(2009, 11, 1), self.medicine.initial_dispense_date())
        
    def test_possession_ratio_lower_bound_date(self):
        when(self.medicine).possession_effective_end_date().thenReturn(date(2009, 12, 30))
        self.assertEquals(date(2009, 10, 1), self.medicine.possession_ratio_lower_bound_date(90))
        
    def test_possession_effective_start_date_when_initial_dispense_date_after_lower_bound(self):
        when(self.medicine).possession_ratio_lower_bound_date(90).thenReturn(date(2009, 11, 30))
        self.medicine.add_prescription(Prescription(dispense_date = date(2009, 12, 01), days_supply = 30))
        self.assertEquals(self.medicine.initial_dispense_date(), self.medicine.possession_effective_start_date(90))

    def test_possession_effective_start_date_when_initial_dispense_date_before_lower_bound(self):
        when(self.medicine).possession_ratio_lower_bound_date(90).thenReturn(date(2009, 12, 30))
        self.medicine.add_prescription(Prescription(dispense_date = date(2009, 12, 01), days_supply = 30))
        self.assertEquals(date(2009, 12, 30), self.medicine.possession_effective_start_date(90))

    def test_prescriptions_in_range(self):
        when(self.medicine).possession_effective_end_date().thenReturn(date(2009, 12, 15))
        p1 = Prescription(dispense_date = date(2009, 8, 1),  days_supply = 30)
        p2 = Prescription(dispense_date = date(2009, 11, 1), days_supply = 30)
        p3 = Prescription(dispense_date = date(2009, 12, 1), days_supply = 30)
        self.medicine.add_prescription(p1)
        self.medicine.add_prescription(p2)
        self.medicine.add_prescription(p3)
        self.assertEquals([p2, p3], self.medicine.prescriptions_in_range(90))
        
    def test_dates_prescribed(self):
        self.medicine.add_prescription(Prescription(dispense_date = date(2009, 12, 1), days_supply = 2))
        self.assertEquals([date(2009, 12, 1), date(2009, 12, 2)], self.medicine.dates_prescribed(2))
        
    def test_dates_prescribed_when_dates_overlap(self):
        self.medicine.add_prescription(Prescription(dispense_date = date(2009, 12, 1), days_supply = 2))
        self.medicine.add_prescription(Prescription(dispense_date = date(2009, 12, 2), days_supply = 2))
        self.assertEquals([date(2009, 12, 1), date(2009, 12, 2), date(2009, 12, 3)], self.medicine.dates_prescribed(5))
    
    def test_dates_prescribed_in_effective_range(self):
        self.medicine.add_prescription(Prescription(dispense_date = date.today() - timedelta(days=2), days_supply = 4))
        self.assertEquals([date.today() - timedelta(days=2), date.today() - timedelta(days=1)], 
                            self.medicine.dates_prescribed_in_effective_range(2))
                            
    def test_number_of_days_prescribed(self):
        when(self.medicine)._possession_effective_range(90).thenReturn([date(2009, 10, 3) + timedelta(days=i) for i in range(75)])
        self.medicine.add_prescription(Prescription(dispense_date = date(2009, 10, 3), days_supply = 30))
        self.medicine.add_prescription(Prescription(dispense_date = date(2009, 11, 17), days_supply = 30))
        self.assertEquals(60, self.medicine.number_of_days_prescribed(90))
        
        
        
if __name__ == "__main__":
    unittest.main()