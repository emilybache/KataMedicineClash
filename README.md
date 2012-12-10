This Kata is included in my book ["The Coding Dojo Handbook"](http://leanpub.com/codingdojohandbook). 

- In the folder for each language, are skeleton classes for the domain objects, to get you started on the kata.
- In the folder "Refactoring" is a refactoring version of this kata
- In the folder "SampleVisualization", is some Python code that can create a graph to visualize a medicine clash.

# Kata: Medicine Clash

__As a__ Health Insurer,

__I want__ to be able to search for patients who have a medicine clash,

__So that__ I can alert their doctors and get their prescriptions changed.

Health Insurance companies don't always get such good press, but in this case, they actually do have your best interests at heart. Some medicines interact in unfortunate ways when they get into your body at the same time, and your doctor isn't always alert enough to spot the clash when writing your prescriptions. Sometimes, medicine interactions are only identified years after the medicines become widely used, and your doctor might not be completely up to date. Your Health Insurer certainly wants you to stay healthy, so discovering a customers has a medicine clash and getting it corrected is good for business, and good for you!

For this Kata, you have a recently discovered medicine clash, and you want to look through a database of patient medicine and prescription records, to find if any need to be alerted to the problem. Create a "Patient" class, with a method "Clash" that takes as arguments a list of medicine names, and how many days before today to consider, (defaults to the last 90 days). It should return a collection of days on which all the medicines were being taken during this time.

# Doing this kata on cyber-dojo

As an alternative to downloading the code, click one of the links below to create a new cyber-dojo to work in, then press "start" to get going coding.

- [Python](http://cyber-dojo.com/forker/fork/0B0F2D70B1?avatar=lion&tag=2)
- [Ruby](http://cyber-dojo.com/forker/fork/DFDB32D26B?avatar=elephant&tag=9)
- [C++](http://www.cyber-dojo.com/forker/fork/E733A0E0C5?avatar=koala&tag=15)
- [Java](http://cyber-dojo.com/forker/fork/87DE97E099?avatar=lion&tag=34)

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

#### You can assume:

- patients start taking the medicine on the dispense date.
- the "days supply" tells you how many days they continue to take the medicine after the dispense date.
- if they have two overlapping prescriptions for the same medicine, they stop taking the earlier one. Imagine they have mislaid the medicine they got from the first prescription when they start on the second prescription.

