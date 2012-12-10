#include "all_tests.hpp"
#include <cassert>
#include <iostream>

typedef void test();

static test * tests[ ] =
{
    /* list all your test cases here */
    test_patient_clash,
    static_cast<test*>(0),
};

int main()
{
    size_t at = 0;
    while (tests[at])
    {
        tests[at++]();
        std::cout << '.';
    }
    std::cout << std::endl << at << " tests passed" << std::endl;
    return 0;
}