#include "Patient.hpp"

#include <chrono>
#include <string>
#include <vector>

using namespace std;
using std::chrono::system_clock;

Patient::Patient(string const & name) : name_(name)
{
}

vector<time_t> Patient::clash(vector<string> medicineNames, int daysBack) const
{
    /* TODO: write this code */
    vector<time_t> dates;
    return dates;
}

void Patient::addMedicine(Medicine medicine)
{
    medicines_.push_back(medicine);
}
