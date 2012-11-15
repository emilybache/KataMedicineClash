
class Medicine(object):
    
    def __init__(self, name):
        self.name = name
        self.prescriptions = []
        
    def add_prescription(self, prescription):
        self.prescriptions.append(prescription)
        