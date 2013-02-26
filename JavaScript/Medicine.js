function Medicine(name) {
    "use strict";

    this.prescriptions = [];
    this.name = name;

}

Medicine.prototype.getName = function () {
    return this.name;
}

Medicine.prototype.addPrescription = function (prescription) {
    this.prescriptions.push(prescription);
}

// var med = Object.create(Medicine.prototype);