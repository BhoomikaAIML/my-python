#inheritance
class parent:
  def function(self):
    print("i am good")
class child(parent):
  def function(self):
    print("i am bad")
obj=parent()
a=child()
obj.function()
a.function()
#output
i am good
i am bad
