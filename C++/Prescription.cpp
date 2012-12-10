#include "Prescription.hpp"

#include <chrono>

using namespace std;

Prescription::Prescription(time_t dispenseDate, int daysSupply)
    : dispenseDate_(dispenseDate)
{
    expirationDate_ = chrono::system_clock::to_time_t(
        chrono::system_clock::from_time_t(dispenseDate) +
        chrono::hours(24 * daysSupply)
        );
}