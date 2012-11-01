require_relative "days_ago"
require_relative "patient"
require_relative "medicine"
require_relative "prescription"

describe Patient do
  describe "#clash" do
      before do
      @patient = Patient.new
      @medicine = Medicine.new(:name => "Codeine")
    end

    context "full possession" do
      before do
        @medicine.prescriptions << Prescription.new(:dispense_date => 30.days.ago.to_date, :days_supply => 30)
        @medicine.prescriptions << Prescription.new(:dispense_date => 60.days.ago.to_date, :days_supply => 30)
        @medicine.prescriptions << Prescription.new(:dispense_date => 90.days.ago.to_date, :days_supply => 30)
        @patient.medicines << @medicine
      end

      it "returns all the days" do
        subject.clash([@medicine], 90).should == 90
      end
    end

    context "partial possession" do
      before do
        @medicine.prescriptions << Prescription.new(:dispense_date => 30.days.ago.to_date, :days_supply => 30)
        @medicine.prescriptions << Prescription.new(:dispense_date => 60.days.ago.to_date, :days_supply => 30)
        @patient.medicines << @medicine
      end

      it "returns two thirds of the days" do
        subject.clash([@medicine], 90).should == 60
      end
    end

  end
end
