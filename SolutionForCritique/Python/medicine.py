from datetime import date, timedelta

class Medicine(object):
    
    def __init__(self, name):
        self.name = name
        self.prescriptions = []
        
    def add_prescription(self, prescription):
        self.prescriptions.append(prescription)
        
    def first_prescription(self):
        self.prescriptions.sort()
        return self.prescriptions[0]
        
    def possession_end_date(self):
        return self.most_recent_prescription().completion_date()
        
    def most_recent_prescription(self):
        self.prescriptions.sort()
        return self.prescriptions[-1]
        
    def possession_effective_end_date(self):
        return min(self.possession_end_date(), date.today())
        
    def initial_dispense_date(self):
        return self.first_prescription().dispense_date
    
    def possession_ratio_lower_bound_date(self, day_count):
        return self.possession_effective_end_date() - timedelta(days=day_count)
        
    def possession_effective_start_date(self, day_count):
        return max(self.possession_ratio_lower_bound_date(day_count), self.initial_dispense_date())

    def prescriptions_in_range(self, day_count):
        possession_effective_range = self._possession_effective_range(day_count)
        return filter(lambda p: 
            p.dispense_date in possession_effective_range
              or p.completion_date() in possession_effective_range, self.prescriptions)
      
    def _possession_effective_range(self, day_count):
        start_date = self.possession_effective_start_date(day_count)
        end_date = self.possession_effective_end_date()
        return [start_date + timedelta(days=i) for i in range(0, (end_date - start_date).days)]
 
    def dates_prescribed(self, day_count):
        dates = set()
        for p in self.prescriptions_in_range(day_count):
            dates = dates.union(set([p.dispense_date + timedelta(days=i) for i in range(p.days_supply)]))
        return sorted(list(dates))
        
    def dates_prescribed_in_effective_range(self, day_count):
        possession_effective_range = self._possession_effective_range(day_count)
        return filter(lambda d: d in possession_effective_range, self.dates_prescribed(day_count))

    def number_of_days_prescribed(self, day_count):
        return len(self.dates_prescribed_in_effective_range(day_count))
