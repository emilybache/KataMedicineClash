require 'bigdecimal'
require 'rspec'
require 'mocha/api'

require_relative "days_ago"
require_relative "patient"
require_relative "medicine"
require_relative "prescription"

describe Medicine do
  describe "#possession_end_date" do
    let(:medicine) do
      Medicine.new("Aspirin").tap do |m|
        m.prescriptions << Prescription.new(:dispense_date => Date.strptime('12/01/2009', '%m/%d/%Y'), :days_supply => 30)
      end
    end
  
    it "returns the sum of the most recent prescription's dispense date and its days supply" do
      medicine.possession_end_date.should == Date.strptime('12/31/2009', '%m/%d/%Y')
    end
  end
  
  describe "#possession_effective_end_date" do
    context "when ending before today's date" do
      let(:medicine) do
        Medicine.new("Aspirin").tap do |m|
          m.prescriptions << Prescription.new(:dispense_date => 40.days.ago, :days_supply => 30)
        end
      end
  
      it "returns the end date" do
        medicine.possession_effective_end_date.should == medicine.possession_end_date
      end
    end
    context "when in theory it would end after today's date" do
      let(:medicine) do
        Medicine.new("Aspirin").tap do |m|
          m.prescriptions << Prescription.new(:dispense_date => 15.days.ago, :days_supply => 30)
        end
      end
  
      it "returns today's date" do
        medicine.possession_effective_end_date.should == Date.today
      end
    end
  end
  
  describe "#initial_dispense_date" do
    let(:medicine) do
      Medicine.new("Aspirin").tap do |m|
        m.prescriptions << Prescription.new(:dispense_date => Date.strptime('11/01/2009', '%m/%d/%Y'), :days_supply => 30)
        m.prescriptions << Prescription.new(:dispense_date => Date.strptime('11/30/2009', '%m/%d/%Y'), :days_supply => 30)
      end
    end
  
    it "returns the first prescriptions dispense date" do
      medicine.initial_dispense_date.should == Date.strptime('11/01/2009', '%m/%d/%Y')
    end
  end
  
  describe "#possession_ratio_lower_bound_date" do
    let(:medicine) do
      Medicine.new("Aspirin").tap do |m|
        m.stubs(:possession_effective_end_date).returns(Date.strptime('12/30/2009', '%m/%d/%Y'))
      end
    end
    it "is the difference of effective end date and the day count" do
      medicine.possession_ratio_lower_bound_date(90).should == Date.strptime('10/01/2009', '%m/%d/%Y')
    end
  end
  
  describe "#possession_effective_start_date" do
    context "when the initial dispense date is after the lower bound date" do
      let(:medicine) do
        Medicine.new("Aspirin").tap do |m|
          m.prescriptions << Prescription.new(:dispense_date => Date.strptime('12/01/2009', '%m/%d/%Y'), :days_supply => 30)
          m.stubs(:possession_ratio_lower_bound_date).returns(Date.strptime('11/30/2009', '%m/%d/%Y'))
        end
      end
      it "returns the initial dispense date" do
        medicine.possession_effective_start_date(90).should == medicine.initial_dispense_date
      end
    end
    context "when the initial dispense date is before the lower bound date" do
      let(:medicine) do
        Medicine.new("Aspirin").tap do |m|
          m.prescriptions << Prescription.new(:dispense_date => Date.strptime('12/01/2009', '%m/%d/%Y'), :days_supply => 30)
          m.stubs(:possession_ratio_lower_bound_date).returns(Date.strptime('12/30/2009', '%m/%d/%Y'))
        end
      end
      it "returns the lower bound date" do
        medicine.possession_effective_start_date(90).should == Date.strptime('12/30/2009', '%m/%d/%Y')
      end
    end
  end
  
  describe "#prescriptions_in_range" do
    let(:medicine) do
      Medicine.new("Aspirin").tap do |m|
        m.prescriptions << @prescription1 = Prescription.new(:dispense_date => Date.strptime('08/01/2009', '%m/%d/%Y'), :days_supply => 30)
        m.prescriptions << @prescription2 = Prescription.new(:dispense_date => Date.strptime('11/01/2009', '%m/%d/%Y'), :days_supply => 30)
        m.prescriptions << @prescription3 = Prescription.new(:dispense_date => Date.strptime('12/01/2009', '%m/%d/%Y'), :days_supply => 30)
        m.stubs(:possession_effective_end_date).returns(Date.strptime('12/15/2009', '%m/%d/%Y'))
      end
    end
    it "returns prescriptions dispensed during the effective range" do
      medicine.prescriptions_in_range(90).should == [@prescription2,@prescription3]
    end
  end
  
  describe "#dates_prescribed" do
    let(:medicine) do
      Medicine.new("Aspirin").tap do |m|
        m.prescriptions << Prescription.new(:dispense_date => Date.strptime('12/01/2009', '%m/%d/%Y'), :days_supply => 2)
      end
    end
    it "returns the Dates a medicine was prescribed for" do
      medicine.dates_prescribed(2).should == [Date.strptime('12/01/2009', '%m/%d/%Y'), Date.strptime('12/02/2009', '%m/%d/%Y')]
    end
  
    context "when there is a date overlap between two prescriptions" do
      let(:medicine) do
        Medicine.new("Aspirin").tap do |m|
          m.prescriptions << Prescription.new(:dispense_date => Date.strptime('12/01/2009', '%m/%d/%Y'), :days_supply => 2)
          m.prescriptions << Prescription.new(:dispense_date => Date.strptime('12/02/2009', '%m/%d/%Y'), :days_supply => 2)
        end
      end
      it "removes duplicates" do
        medicine.dates_prescribed(5).should == [Date.strptime('12/01/2009', '%m/%d/%Y'), 
                                                Date.strptime('12/02/2009', '%m/%d/%Y'), 
                                                Date.strptime('12/03/2009', '%m/%d/%Y')]
      end
    end
  end

  describe "#dates_prescribed_in_effective_range" do
      let(:medicine) do
        Medicine.new("Aspirin").tap do |m|
          m.prescriptions << Prescription.new(:dispense_date => 2.days.ago, :days_supply => 4)
        end
      end
    it "returns the Dates a medicine was prescribed that fall in the effective possession range" do
      medicine.dates_prescribed_in_effective_range(2).should == [2.days.ago, 1.day.ago]
    end
  end


  describe "#number_of_days_prescribed(90)" do
    let(:medicine) do
      Medicine.new("Aspirin").tap do |m|
        m.stubs(:possession_effective_range).returns(Date.strptime('10/03/2009', '%m/%d/%Y')..Date.strptime('12/17/2009', '%m/%d/%Y'))
        m.prescriptions << Prescription.new(:dispense_date => Date.strptime('10/03/2009', '%m/%d/%Y'), :days_supply => 30)
        m.prescriptions << Prescription.new(:dispense_date => Date.strptime('11/17/2009', '%m/%d/%Y'), :days_supply => 30)
      end
    end
    it "returns a count of the days that a medicine was prescribed that fall in the effective possession range" do
      medicine.number_of_days_prescribed(90).should == 60
    end
  end
  
end