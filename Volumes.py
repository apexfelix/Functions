#Area of circle
def Area():
  pi=3.142
  r=(input("Enter value"))
  a=pi*int(r)*int(r)
  print("Area is",a)
Area()
print("_______________")
#Volume of cylinder
def Volume():
  pi=3.142
  r=(input("Enter Radius"))
  h=(input("Enter Height"))
  v=pi*int(r)*int(r)*int(h)
  print("Volume is",v)
Volume()
print("___________________")
#Volume of Sphere
def VolumeSphere():
  pi=3.142
  r=(input("Enter Radius"))
  v=4/3*pi*int(r)*int(r)*int(r)
  print("Volume Sphere is",v)
VolumeSphere()