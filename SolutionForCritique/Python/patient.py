
class Patient(object):
    
    def __init__(self, medicines = None):
        self._medicines = medicines or []
    
    def add_medicine(self, medicine):
        self._medicines.append(medicine)
    
    def clash(self, medicines, days):
        if not medicines:
            return set()
        dates = set.intersection(*[set(medicine.dates_prescribed_in_effective_range(days)) for medicine in medicines])
        return dates
