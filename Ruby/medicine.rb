class Medicine
  
  attr_reader :name, :prescriptions
  
  def initialize(name)
    @name = name
    @prescriptions = []
  end
  
end