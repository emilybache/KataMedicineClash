require_relative "days_ago"
require_relative "patient"
require_relative "medicine"
require_relative "prescription"

describe Patient do
  before do
    @patient = Patient.new
    @codeine = Medicine.new("Codeine")
    @prozac = Medicine.new("Prozac")
    @patient.medicines << @codeine
    @patient.medicines << @prozac
  end

  describe "#clash" do
    context "no prescriptions" do
      it "returns an empty list of dates" do
        @patient.clash(["Codeine", "Prozac"], 90).should == []
      end
    end

    context "only one medicine being taken" do
      before do
        @codeine.prescriptions << Prescription.new(:dispense_date => 30.days.ago, :days_supply => 30)
      end

      it "returns an empty list of days" do
        @patient.clash(["Codeine", "Prozac"], 90).size.should == 0
      end
    end

    context "both medicines taken but with no overlap" do
      before do
        @codeine.prescriptions << Prescription.new(:dispense_date => 30.days.ago, :days_supply => 30)
        @prozac.prescriptions << Prescription.new(:dispense_date => 90.days.ago, :days_supply => 30)
      end

      it "returns an empty list of days" do
        @patient.clash(["Codeine", "Prozac"], 90).size.should == 0
      end
    end

    context "both medicines taken continuously" do
      before do
        @codeine.prescriptions << Prescription.new(:dispense_date => 30.days.ago, :days_supply => 30)
        @codeine.prescriptions << Prescription.new(:dispense_date => 60.days.ago, :days_supply => 30)
        @codeine.prescriptions << Prescription.new(:dispense_date => 90.days.ago, :days_supply => 30)
        @prozac.prescriptions << Prescription.new(:dispense_date => 30.days.ago, :days_supply => 30)
        @prozac.prescriptions << Prescription.new(:dispense_date => 60.days.ago, :days_supply => 30)
        @prozac.prescriptions << Prescription.new(:dispense_date => 90.days.ago, :days_supply => 30)
      end

      it "returns all the days" do
        @patient.clash(["Codeine", "Prozac"], 90).size.should == 90
      end
    end

    context "one medicine taken only on some of the days" do
      before do
        @codeine.prescriptions << Prescription.new(:dispense_date => 30.days.ago, :days_supply => 30)
        @codeine.prescriptions << Prescription.new(:dispense_date => 60.days.ago, :days_supply => 30)
        @prozac.prescriptions << Prescription.new(:dispense_date => 30.days.ago, :days_supply => 30)
        @prozac.prescriptions << Prescription.new(:dispense_date => 60.days.ago, :days_supply => 30)
        @prozac.prescriptions << Prescription.new(:dispense_date => 90.days.ago, :days_supply => 30)
      end

      it "returns two thirds of the days" do
        @patient.clash(["Codeine", "Prozac"], 90).size.should == 60
      end
    end

    context "two medicines taken in a partially overlapping period" do
      before do
        @codeine.prescriptions << Prescription.new(:dispense_date => 30.days.ago, :days_supply => 30)
        @prozac.prescriptions << Prescription.new(:dispense_date => 40.days.ago, :days_supply => 30)
      end

      it "returns only the days both were taken" do
        @patient.clash(["Codeine", "Prozac"], 90).size.should == 20
      end
    end
    
    context "two medicines overlapping with current date" do
      before do
        @codeine.prescriptions << Prescription.new(:dispense_date => 1.day.ago, :days_supply => 30)
        @prozac.prescriptions << Prescription.new(:dispense_date => 5.days.ago, :days_supply => 30)
      end

      it "returns only the days both were taken, not future dates" do
        @patient.clash(["Codeine", "Prozac"], 90).should == [1.day.ago]
      end
    end
    context "two medicines overlapping with start of period" do
      before do
        @codeine.prescriptions << Prescription.new(:dispense_date => 91.day.ago, :days_supply => 30)
        @prozac.prescriptions << Prescription.new(:dispense_date => 119.days.ago, :days_supply => 30)
      end

      it "returns only the days both were taken that fall within the last 90 days" do
        @patient.clash(["Codeine", "Prozac"], 90).should == [90.days.ago]
      end
    end
  end

  describe "#medicines_taken_from" do
    context "emty list of names" do
      it "returns an empty list of medicines" do
        @patient.medicines_taken_from([]).should == []
      end
    end

    context "two medicines that are being taken" do
      it "returns the medicines on the list" do
        @patient.medicines_taken_from(["Codeine", "Prozac"]).should == [@codeine, @prozac]
      end
    end

    context "two medicines, one is not being taken" do
      it "returns the medicine that is being taken" do
        @patient.medicines_taken_from(["Codeine", "foo"]).should == [@codeine]
      end
    end
  end

end
