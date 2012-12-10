#include "Prescription.hpp"

#include <string>
#include <vector>

class Medicine
{
    std::string name_;
    std::vector<Prescription> prescriptions_;
public:

    explicit Medicine(std::string const & name);

    void addPrescription(Prescription prescription);
    std::string getName() const;
    void getOverlappingPrescriptionDays(Medicine const & rhs, std::vector<std::time_t> & overlap) const;
};