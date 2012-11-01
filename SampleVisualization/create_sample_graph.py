from datetime import date, timedelta
import matplotlib.pyplot as plt

from patient import Patient, Prescription

def plot(patient, medicine_names, filename):
    day_zero = date.today().toordinal()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    for i, medicine_name in enumerate(medicine_names):
        prescriptions = filter(lambda p: p.name == medicine_name, patient.prescriptions)
        days_to_plot = [(p.dispense_date.toordinal()-day_zero, p.days_supply) for p in prescriptions]
        ax.broken_barh(days_to_plot, (10*(i+1), 9), facecolors=['red', 'yellow', 'green', 'blue', 'orange'][i])
    
    days_taking_all = []
    days_taking_all = sorted([(day.toordinal()-day_zero, 1) for day in patient.days_taking_all(medicine_names)])
    ax.broken_barh(days_taking_all, (0, 9), facecolors='black')
    
    medicine_count = len(medicine_names)
    ax.set_ylim(-5,10*(medicine_count+1)+5)
    ax.set_xlim(-110,0)
    ax.set_xlabel('relative to today')
    ax.set_yticks([i*10+5 for i in range(medicine_count+2)])
    ax.set_yticklabels(["clash"] + medicine_names)
    ax.grid(True)

    fig.savefig(filename)

if __name__ == "__main__":
    patient = Patient()
    patient.add_prescription(Prescription("Aspirin", dispense_date=date.today() - timedelta(100), days_supply = 20))
    patient.add_prescription(Prescription("Aspirin", dispense_date=date.today() - timedelta(50), days_supply = 50))
    patient.add_prescription(Prescription("Codeine", dispense_date=date.today() - timedelta(15), days_supply = 3))
    patient.add_prescription(Prescription("Codeine", dispense_date=date.today() - timedelta(60), days_supply = 3))
    patient.add_prescription(Prescription("Codeine", dispense_date=date.today() - timedelta(30), days_supply = 3))
    plot(patient, ["Aspirin", "Codeine"], "graph.png")
