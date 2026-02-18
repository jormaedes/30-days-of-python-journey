# ============================================================
# Day 3 - Operators | 30 Days of Python
# ============================================================

# Exercise 1
age = 25
print(type(age))

# Exercise 2
height = 1.77
print(type(height))

# Exercise 3
comp = 1 + 2j
print(type(comp))

# Exercise 4
b = int(input('Enter base: '))
h = int(input('Enter height:'))
area = 0.5 * b * h
print('The area of the triangle is', area)

# Exercise 5
a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))
perim = a + b + c
print('The perimeter of the triangle is', perim)

# Exercise 6
length = float(input('Enter length: '))
width = float(input('Enter width: '))
area = length * width
perim = 2 * (length + width)
print('Area: ', area)
print('Perimeter: ', perim)

# Exercise 7
radius = float(input('Enter radius: '))
area = 3.14 * radius * radius
circum = 2 * 3.14 * radius
print('Area: ', area)
print('Circumference: ', circum)

# Exercise 8
# Forma geral: y = mx + b  →  y = 2x - 2
# slope (m) = 2
# y-intercept: quando x = 0  →  y = 2(0) - 2 = -2
# x-intercept: quando y = 0  →  0 = 2x - 2  →  x = 1
slope = 2
y_intercept = -2
x_intercept = 1
print(f"Slope: {slope}")
print(f"X-intercept: {x_intercept}")
print(f"Y-intercept: {y_intercept}")

# Exercise 9
x1, y1 = 2, 2
x2, y2 = 6, 10
point_slope = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f"Slope between (2,2) and (6,10): {point_slope}")
print(f"Euclidean distance: {euclidean_distance}")

# Exercise 10
print(point_slope == slope)

# Exercise 11
x = -3
y = x ** 2 + 6 * x + 9

# Exercise 12
len_p = len('python')
len_d = len('dragon')
print(len_p != len_d)

# Exercise 13
print(('on' in 'python') and ('on' in 'dragon'))

# Exercise 14
print('jargon' in 'I hope this course is not full of jargon')

# Exercise 15
print(('on' not in 'python') and ('on' not in 'dragon'))

# Exercise 16
len_p = len('python')
fl = float(len_p)
st = str(fl)

# Exercise 17
n = 10
print(n % 2 == 0)

# Exercise 18
print(7 // 3 == int(2.7))

# Exercise 19
print(type('10') == type(10))

# Exercise 20
print(int('9.8') == 10)

# Exercise 21
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
print(f"Your weekly earning is {weekly_earning}")

# Exercise 22
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")

# Exercise 23
# Simplesmente mandaram fazer a saida dessa forma, então não estou errado kkkk
print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')

