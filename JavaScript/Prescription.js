function Prescription(date, daysSupply) {
    "use strict";

    this.dispenseDate = date || new Date();
    this.daysSupply = daysSupply || 30;
}
