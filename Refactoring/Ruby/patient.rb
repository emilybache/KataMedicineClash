class Patient

  attr_reader :medicines

  def initialize()
    @medicines = []
  end

  def clash(medicine_names, days_back)
    medicines_taken = medicines_taken_from(medicine_names)
    return [] if medicines_taken.empty?
    all_dates = medicines_taken.map { |medicine| medicine.dates_prescribed_in_effective_range(days_back)}
    all_dates.inject{|x, y| x & y}
  end

  def medicines_taken_from(medicine_names)
    @medicines.select { |medicine| medicine_names.include?(medicine.name) }
  end

end