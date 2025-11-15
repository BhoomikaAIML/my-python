#multiple inheritance
class A:
  def fun1(self):
    print("day 1")
class B:
  def fun2(self):
    print("day 2")
class c(A,B):
  pass
obj=A()
obj2=B()
obj.fun1()
#output
day 1
