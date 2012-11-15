
from datetime import date

class Prescription(object):
    
    def __init__(self, dispense_date=None, days_supply=30):
        self.dispense_date = dispense_date or date.today()
        self.days_supply = days_supply
