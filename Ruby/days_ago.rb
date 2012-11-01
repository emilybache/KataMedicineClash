require 'date'

class Fixnum
  def day
     days
  end

  def days
     self
  end

  def ago
    Date.today - self
  end
  
  def from_now
    Date.today + self
  end
end

class Date
  def advance(options={})
    self + (options[:days] || 0)
  end
end
