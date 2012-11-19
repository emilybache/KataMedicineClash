from datetime import timedelta, date

class Prescription(object):
    
    def __init__(self, dispense_date=None, days_supply=30):
        self.dispense_date = dispense_date or date.today()
        self.days_supply = days_supply
    
    def completion_date(self):
        return self.dispense_date + timedelta(days = self.days_supply)
        
    def days_taken(self):
        return [self.dispense_date + timedelta(days=i) for i in range(self.days_supply)]
        
    def __cmp__(self, other):
        return cmp(self.dispense_date, other.dispense_date)