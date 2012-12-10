

import java.util.ArrayList;
import java.util.Collection;
import java.util.Date;

public class Patient {

    private Collection<Medicine> medicines = new ArrayList<Medicine>();

    public void addMedicine(Medicine medicine) {
        this.medicines.add(medicine);
    }

    public Collection<Date> clash(Collection<String> medicineNames) {
        return clash(medicineNames, 90);
    }

    public Collection<Date> clash(Collection<String> medicineNames, int daysBack) {
        // TODO: implement this method
        return null;
    }


}
