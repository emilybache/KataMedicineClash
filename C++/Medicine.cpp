#include "Medicine.hpp"

using namespace std;

Medicine::Medicine(string const & name) : name_(name)
{
}

void Medicine::addPrescription(Prescription prescription)
{
    prescriptions_.push_back(prescription);
}

string Medicine::getName() const
{
    return name_;
}