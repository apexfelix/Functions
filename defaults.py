#Abitary arguments
def table(*PL):
  for teams in PL:
    print(teams)
table("Man City", "Man Utd", "Leicester", "Chelsea")
print("_____________________________________")
def courses(**kwargs):
  for key, value in kwargs.items():
    print("{}:{}".format(key,value))
courses(first="BSCIT",second="CCNA",third="BBIT")
#Default parameter value
def kenya(County="Siaya"):
  print("I am from "+County)
kenya()
kenya("Nairobi")
kenya("Kisumu")
kenya("Kiambu")
kenya("Mombasa")
#passing list as Argument
def my_function(food):
  for x in food:
    print(x)
fruits=["apples","banana","cherry"]
county_code={
"Mombasa":"001",
"Nairobi":"047",
"Siaya":"043",
}
my_function(fruits)
my_function(county_code)