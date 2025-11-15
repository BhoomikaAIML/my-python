#oops
class area_of_circle:
  def __init__(self, radius): 
    self.radius=radius
  def circle(self):
    return 3.14*self.radius*self.radius
area = area_of_circle(8)
area.circle()
#output
200.96
