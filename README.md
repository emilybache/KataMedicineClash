This is a sample solution to the Kata "MedicineClash". This Kata is included in my book "The Coding Dojo Handbook", available from [LeanPub](http://leanpub.com/codingdojohandbook). Further down this page you will find a description of the kata. When you have done it for yourself, you may find these sample solutions more interesting.

To run the tests for the Python version, you will need to install [mockito](http://code.google.com/p/mockito-python/).

To run the tests for the Ruby version, you will need to install these gems:

- rspec
- mocha

There is also some code that can create a graph to visualize a medicine clash. To run the code, you will need to install [matplotlib](http://matplotlib.org/). To run the tests for this code, you will need to install [py.test](http://pytest.org)


# Kata: Medicine Clash

__As a__ Health Insurer,

__I want__ to be able to search for patients who have a medicine clash,

__So that__ I can alert their doctors and get their prescriptions changed.

Health Insurance companies don't always get such good press, but in this case, they actually do have your best interests at heart. Some medicines interact in unfortunate ways when they get into your body at the same time, and your doctor isn't always alert enough to spot the clash when writing your prescriptions. Often, medicine interactions are only identified years after the medicines become widely used, and your doctor might not be completely up to date. Your Health Insurer certainly wants you to stay healthy, so discovering a customers has a medicine clash and getting it corrected is good for business, and good for you!

For this Kata, your task is to search a database of patient records and find the ones that have recently been taking prescription medicines that clash. For each patient, look at the most recent 90 days, and calculate the number of days they have taken all of a list of medicines that are known to clash.

## Data Format

You can assume the data is in a database, which is accessed in the code via an object oriented domain model. The domain model is large and complex, but for this problem you can ignore all but the following entities and attributes:

    Patient
    + medicines

    Medicine
    + name
    + prescriptions

    Prescription
    + dispense date
    + days supply


So each Patient has a list of Medicines. Medicines have a unique name. Each Medicine has a list of Prescriptions. Each Prescription has a dispense date and a number of days supply.
    
Alternatively the data could be in a .csv file with column headings like this: 

    patient id, medicine name, prescription, dispense date, days supply 
    
There would be one row in the file for each prescription, ie several rows for each patient. The "dispense date" could be listed in ISO format to make it easy to parse, eg 2012-11-01.

#### You can assume:

- patients start taking the medicine on the dispense date.
- the "days supply" tells you how many days they continue to take the medicine after the dispense date.
- if they have two overlapping prescriptions for the same medicine, they stop taking the earlier one. Imagine they have mislaid the medicine they got from the first prescription when they start on the second prescription.