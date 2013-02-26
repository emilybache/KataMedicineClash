function Patient() {
    "use strict";

    this.medicines = [];
}

Patient.prototype.addMedicine = function (medicine) {
    "use strict";

    this.medicines.push(medicine);
};

Patient.prototype.clash = function (medicineNames, days) {
    "use strict";

    if (typeof days === "number") {
        // TODO with days
    } else {
        // TODO without days
    }
}