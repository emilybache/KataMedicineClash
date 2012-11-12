from datetime import date, timedelta

class Prescription:
    
    def __init__(self, name, dispense_date, days_supply):
        self.name = name
        self.dispense_date = dispense_date
        self.days_supply = days_supply
        
    def days_taken(self):
        return [self.dispense_date + timedelta(days=i) for i in range(self.days_supply)]

class Patient:
    
    def __init__(self, prescriptions=None):
        self.prescriptions = prescriptions or []
    
    def add_prescription(self, prescription):
        self.prescriptions.append(prescription)
        
    def days_taking(self, medicine_name):
        prescriptions = filter(lambda p: p.name == medicine_name, self.prescriptions)
        days = set()
        for prescription in prescriptions:
            days.update(prescription.days_taken())
        return days
        
    def clash(self, medicine_names):
        days_taking = [self.days_taking(medicine_name) for medicine_name in medicine_names] or [set()]
        return set.intersection(*days_taking)
