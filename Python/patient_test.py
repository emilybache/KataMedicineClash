import unittest
from datetime import date, timedelta

from patient import *
from medicine import Medicine
from prescription import Prescription

class PatientTest(unittest.TestCase):
    
    def setUp(self):
        self.patient = Patient()
        self.medicine = Medicine("Aspirin")
        self.patient.add_medicine(self.medicine)
    
    def test_clash_when_full(self):
        self.medicine.add_prescription(Prescription(dispense_date=(date.today() - timedelta(days=30)), days_supply=30))
        self.medicine.add_prescription(Prescription(dispense_date=(date.today() - timedelta(days=60)), days_supply=30))
        self.medicine.add_prescription(Prescription(dispense_date=(date.today() - timedelta(days=90)), days_supply=30))
        self.assertEquals(90, self.patient.clash([self.medicine], 90))

    def test_clash_when_partial(self):
        self.medicine.add_prescription(Prescription(dispense_date=(date.today() - timedelta(days=30)), days_supply=30))
        self.medicine.add_prescription(Prescription(dispense_date=(date.today() - timedelta(days=60)), days_supply=30))
        self.assertEquals(60, self.patient.clash([self.medicine], 90))
    
    
if __name__ == "__main__":
    unittest.main()