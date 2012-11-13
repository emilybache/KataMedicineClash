class Patient

  attr_reader :medicines

  def initialize()
    @medicines = []
  end

  def clash(drugs, days)
      return [] if drugs.empty?
      day_count = Date.today - days
      drugs.map { |drug| drug.dates_prescribed_in_effective_range(day_count)}.inject{|x, y| x & y}
    end

end