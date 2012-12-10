class Prescription

  attr_reader :dispense_date, :days_supply

  def initialize(options = {})
    @dispense_date = options[:dispense_date] ||= Date.today
    @days_supply = options[:days_supply] ||= 30
  end

  def <=>(other)
    return -1 if dispense_date.nil?
    return 1 if other.dispense_date.nil?
    dispense_date <=> other.dispense_date
  end

  def completion_date
    dispense_date + days_supply
  end

  def days_taken
    (dispense_date...(dispense_date + days_supply)).to_a
  end
end