#include "Medicine.hpp"

#include <ctime>
#include <string>
#include <vector>

class Patient 
{
    std::string name_;
    std::vector<Medicine> medicines_;
public:

    explicit Patient(std::string const & name);

    std::vector<std::time_t> clash(std::vector<std::string> medicineNames, int daysBack) const;
    void addMedicine(Medicine medicine);

};