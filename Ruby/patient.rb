class Patient

  attr_reader :medicines

  def initialize()
    @medicines = []
  end

  def clash(medicines, days)
      return [] if medicines.empty?
      day_count = Date.today - days
      medicines.map { |medicine| medicine.dates_prescribed_in_effective_range(day_count)}.inject{|x, y| x & y}
    end

end