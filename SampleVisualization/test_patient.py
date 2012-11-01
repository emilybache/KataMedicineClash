from datetime import date, timedelta

from patient import Patient, Prescription

# to run these tests, use py.test (http://pytest.org/)
class TestPatient:
    
    def test_days_taking_all_with_no_prescriptions(self):
        patient = Patient(prescriptions=[])
        assert patient.days_taking_all([]) == set()
        
    def test_days_taking_all_with_one_irrelevant_prescription(self):
        patient = Patient(prescriptions=[Prescription("Paracetamol", dispense_date = date.today() - timedelta(days=2), days_supply=2)])
        assert patient.days_taking_all(["Aspirin"]) == set()
        
    def test_days_taking_all_with_one_prescription(self):
        patient = Patient(prescriptions=[Prescription("Paracetamol", dispense_date = date.today() - timedelta(days=2), days_supply=2)])
        assert patient.days_taking_all(["Paracetamol"]) == set([date.today() - timedelta(days=2), date.today() - timedelta(days=1)])

    def test_days_taking_all_with_two_different_prescriptions(self):
        patient = Patient(prescriptions=[Prescription("Paracetamol", dispense_date = date.today() - timedelta(days=2), days_supply=2),
                                         Prescription("Aspirin",     dispense_date = date.today() - timedelta(days=2), days_supply=2)])
        assert patient.days_taking_all(["Paracetamol", "Aspirin"]) == set([date.today() - timedelta(days=2), date.today() - timedelta(days=1)])

    def test_days_taking_all_with_two_prescriptions_for_same_medication(self):
        patient = Patient(prescriptions=[Prescription("Paracetamol", dispense_date = date.today() - timedelta(days=2), days_supply=2),
                                         Prescription("Paracetamol", dispense_date = date.today() - timedelta(days=3), days_supply=2)])
        assert patient.days_taking_all(["Paracetamol"]) == set([date.today() - timedelta(days=3),
                                                           date.today() - timedelta(days=2), 
                                                           date.today() - timedelta(days=1)])

    def test_days_taking_for_irrelevant_prescription(self):
        patient = Patient(prescriptions=[Prescription("Paracetamol", dispense_date = date.today() - timedelta(days=2), days_supply=2)])
        assert patient.days_taking("Aspirin") == set()

    def test_days_taking(self):
        patient = Patient(prescriptions=[Prescription("Paracetamol", dispense_date = date.today() - timedelta(days=2), days_supply=2),
                                         Prescription("Paracetamol", dispense_date = date.today() - timedelta(days=3), days_supply=2)])
        assert patient.days_taking("Paracetamol") == set([date.today() - timedelta(days=3),
                                                     date.today() - timedelta(days=2), 
                                                     date.today() - timedelta(days=1)])
        