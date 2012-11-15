
class Prescription

  attr_reader :dispense_date, :days_supply

  def initialize(options = {})
    @dispense_date = options[:dispense_date] ||= Date.today
    @days_supply = options[:days_supply] ||= 30
  end

end