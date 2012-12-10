#include "all_tests.hpp"
#include "Patient.hpp"
#include <cassert>
#include <ctime>
#include <chrono>
#include <stdexcept>

using namespace std;
using std::chrono::system_clock;

void test_patient_clash()
{
    system_clock::time_point time_point_now = system_clock::now();
    time_t time_30_days_ago = system_clock::to_time_t(
        time_point_now - chrono::hours(24 * 30)
        );

    Medicine codeine("codeine");
    codeine.addPrescription(Prescription(time_30_days_ago, 30));

    Medicine prozac("prozac");
    prozac.addPrescription(Prescription(time_30_days_ago, 30));

    Patient patient("Bob");
    patient.addMedicine(codeine);
    patient.addMedicine(prozac);
    vector<string> medicine_names;
    medicine_names.push_back("codeine");
    medicine_names.push_back("prozac");

    vector<time_t> clashing_dates = patient.clash(medicine_names, 90);

    assert(clashing_dates.size() == 30);
}

/* add more test cases here */