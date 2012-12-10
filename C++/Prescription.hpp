#include <ctime>
#include <vector>

class Prescription
{
    std::time_t dispenseDate_;
    std::time_t expirationDate_;
public:
    Prescription(std::time_t dispenseDate, int daysSupply);
};
