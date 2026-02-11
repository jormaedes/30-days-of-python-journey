# Dia 2/30 dias de programação em python

## Exercicios: Level 1
firstname = "Jormaedes"
lastname = "Luís"
fullname = firstname + " " + lastname
country = "Angola"
city = "Luanda"
age = 190
year = 2026
is_married, is_true, is_light_on = False, True, True

print("First name: ", firstname)
print("Last name: ", lastname)
print("Full name: ", fullname)
print("Country: ", country)
print("City: ", city)
print("Age: ", age)
print("Year: ", year)
print("Is married: ", is_married)
print("Is True: ", is_true)
print("Is light on: ", is_light_on)

## Exercicios: Level 2
print(type(firstname))
print(type(lastname))
print(type(fullname))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print('len: ', len(firstname))
print(len(firstname) > len(lastname))

num_one, num_two = 5, 4
total = num_one + num_two
diff = num_one - num_two
prod = num_two * num_one
div = num_one / num_two
rest = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

r = 30
_area_of_circle_ = 3.14 * r * r
_circum_of_circle_ = 2 * 3.14 * r

r = float(input("Enter the radius: "))
_area_of_circle_ = 3.14 * r * r
print("Area of Circle: ", _area_of_circle_)

firstname = input("Enter your firstname: ")
lastname = input("Enter your lastname: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))
print("First name: ", firstname)
print("Last name: ", lastname)
print("Country: ", country)
print("Age: ", age)


help('keywords')