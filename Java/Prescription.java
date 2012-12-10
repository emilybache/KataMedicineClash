

import java.util.Date;

public class Prescription {
    
    private Date dispenseDate = new Date();
    private int daysSupply = 30;
    
    public Prescription(Date dispenseDate, int daysSupply) {
        this.dispenseDate = dispenseDate;
        this.daysSupply = daysSupply;
    }

}
