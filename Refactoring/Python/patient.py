
class Patient(object):
    
    def __init__(self, medicines = None):
        self._medicines = medicines or []
    
    def add_medicine(self, medicine):
        self._medicines.append(medicine)
    
    def clash(self, medicine_names, days_back):
        medicines = [medicine for medicine in self._medicines if medicine.name in medicine_names]
        if not medicines:
            return set()
        dates = set.intersection(*[set(medicine.dates_prescribed_in_effective_range(days_back)) for medicine in medicines])
        return dates
