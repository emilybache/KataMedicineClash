import unittest
from datetime import date, timedelta

from patient import *
from medicine import Medicine
from prescription import Prescription

def days_ago(days):
   return date.today() - timedelta(days=days) 

class PatientTest(unittest.TestCase):
    
    def setUp(self):
        self.patient = Patient()
        self.codeine = Medicine("Codeine")
        self.prozac = Medicine("Prozac")
        self.patient.add_medicine(self.codeine)
        self.patient.add_medicine(self.prozac)
    
    def test_no_clash_when_no_overlap(self):
        self.codeine.add_prescription(Prescription(days_ago(30), days_supply=30))
        self.prozac.add_prescription(Prescription(days_ago(90), days_supply=30))
        self.assertEquals(0, len(self.patient.clash([self.codeine, self.prozac], 90)))
 
    def test_no_clash_when_not_taking_both_medicines(self):
        self.codeine.add_prescription(Prescription(days_ago(30), days_supply=30))
        self.assertEquals(0, len(self.patient.clash([self.codeine, self.prozac], 90)))
        
    def test_clash_when_medicines_taken_continuously(self):
        self.codeine.add_prescription(Prescription(days_ago(30), days_supply=30))
        self.codeine.add_prescription(Prescription(days_ago(60), days_supply=30))
        self.codeine.add_prescription(Prescription(days_ago(90), days_supply=30))
        self.prozac.add_prescription(Prescription(days_ago(30), days_supply=30))
        self.prozac.add_prescription(Prescription(days_ago(60), days_supply=30))
        self.prozac.add_prescription(Prescription(days_ago(90), days_supply=30))
        self.assertEquals(90, len(self.patient.clash(["Codeine", "Prozac"], 90)))

    def test_clash_when_one_medicine_taken_on_some_of_the_days(self):
        self.codeine.add_prescription(Prescription(days_ago(30), days_supply=30))
        self.codeine.add_prescription(Prescription(days_ago(60), days_supply=30))
        self.prozac.add_prescription(Prescription(days_ago(30), days_supply=30))
        self.prozac.add_prescription(Prescription(days_ago(60), days_supply=30))
        self.prozac.add_prescription(Prescription(days_ago(90), days_supply=30))
        self.assertEquals(60, len(self.patient.clash(["Codeine", "Prozac"], 90)))

    def test_two_medicines_taken_in_a_partially_overlapping_period(self):
        self.codeine.add_prescription(Prescription(days_ago(30), days_supply=30))
        self.prozac.add_prescription(Prescription(days_ago(40), days_supply=30))
        self.assertEquals(20, len(self.patient.clash(["Codeine", "Prozac"], 90)))

    def test_two_medicines_taken_overlapping_current_date(self):
        self.codeine.add_prescription(Prescription(days_ago(1), days_supply=30))
        self.prozac.add_prescription(Prescription(days_ago(5), days_supply=30))
        self.assertEquals(set([days_ago(1)]), self.patient.clash(["Codeine", "Prozac"], 90))

    def test_two_medicines_taken_overlapping_start_of_period(self):
        self.codeine.add_prescription(Prescription(days_ago(91), days_supply=30))
        self.prozac.add_prescription(Prescription(days_ago(119), days_supply=30))
        self.assertEquals(set([days_ago(90)]), self.patient.clash(["Codeine", "Prozac"], 90))

    
if __name__ == "__main__":
    unittest.main()