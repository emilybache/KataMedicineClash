require_relative "days_ago"
require_relative "patient"
require_relative "medicine"
require_relative "prescription"

describe Patient do
  describe "#clash" do
      before do
      @patient = Patient.new
      @codeine = Medicine.new(:name => "Codeine")
      @prozac = Medicine.new(:name => "Prozac")
      @patient.medicines << @codeine
      @patient.medicines << @prozac
    end

    context "no prescriptions" do
      it "returns an empty list of dates" do
        subject.clash([@codeine, @prozac], 90).should == []
      end
    end

    context "one medicine, taken continuously" do
      before do
        @codeine.prescriptions << Prescription.new(:dispense_date => 30.days.ago.to_date, :days_supply => 30)
        @codeine.prescriptions << Prescription.new(:dispense_date => 60.days.ago.to_date, :days_supply => 30)
        @codeine.prescriptions << Prescription.new(:dispense_date => 90.days.ago.to_date, :days_supply => 30)
      end

      it "returns all the days" do
        subject.clash([@codeine], 90).size.should == 90
      end
    end

    context "one medicine, taken only on some of the days" do
      before do
        @codeine.prescriptions << Prescription.new(:dispense_date => 30.days.ago.to_date, :days_supply => 30)
        @codeine.prescriptions << Prescription.new(:dispense_date => 60.days.ago.to_date, :days_supply => 30)
      end

      it "returns two thirds of the days" do
        subject.clash([@codeine], 90).size.should == 60
      end
    end

    context "two medicines taken in a partially overlapping period" do
      before do
        @codeine.prescriptions << Prescription.new(:dispense_date => 30.days.ago.to_date, :days_supply => 30)
        @prozac.prescriptions << Prescription.new(:dispense_date => 40.days.ago.to_date, :days_supply => 30)
      end

      it "returns only the days both were taken" do
        subject.clash([@codeine, @prozac], 90).size.should == 20
      end
    end
    
    context "two medicines overlapping with current date" do
      before do
        @codeine.prescriptions << Prescription.new(:dispense_date => 1.day.ago.to_date, :days_supply => 30)
        @prozac.prescriptions << Prescription.new(:dispense_date => 5.days.ago.to_date, :days_supply => 30)
      end

      it "returns only the days both were taken, not future dates" do
        subject.clash([@codeine, @prozac], 90).should == [1.day.ago.to_date]
      end
    end
  end
end
