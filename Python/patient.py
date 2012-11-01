
class Patient:
    
    def __init__(self, medicines = None):
        self.medicines = medicines or []
    
    def add_medicine(self, medicine):
        self.medicines.append(medicine)
    
    def clash(self, medicines, days):
        if not medicines:
            return 0
        dates = set()
        for medicine in medicines:
            dates = dates.union(set(medicine.dates_prescribed_in_effective_range(days)))
        return len(dates)
