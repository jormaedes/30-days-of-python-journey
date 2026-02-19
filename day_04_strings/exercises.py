# ============================================================
# Day 4 - Operators | 30 Days of Python
# ============================================================

# Exercise 1
strings = ['Thirty','Days', 'Of', 'Python']
result = ' '.join(strings)
print(result)

# Exercise 2
strings = ['Coding', 'For' , 'All']
result = ' '.join(strings)
print(result)

# Exercise 3
company = "Coding For All"

# Exercise 4
print(company)

# Exercise 5
print(len(company))

# Exercise 6
company_upper = company.upper()

# Exercise 7
company_lower = company.lower()

# Exercise 8
company_capitalize = company.capitalize()
company_swapcase = company.swapcase()
company_title = company.title()

# Exercise 9
print(company[0:6])
print(company_upper[0:6])
print(company_lower[0:6])
print(company_capitalize[0:6])
print(company_swapcase[0:6])
print(company_title[0:6])

# Exercise 10
print('Coding For All '.find('Coding'))

# Exercise 11
company_rpl = company.replace('Coding', 'Python')
print(company_rpl)

# Exercise 12
print('Python for Everyone'.replace('Everyone', 'All'))

# Exercise 13
print('Coding For All'.split())

# Exercise 14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))

# Exercise 15
print('Coding For All'[0])

# Exercise 16
print(len('Coding For All') - 1)

# Exercise 17
print('Coding For All'[10])

# Exercise 18
p_for_all = 'Python For Everyone'

# Exercise 19
c_for_all = 'Coding For All'

# Exercise 20
print(c_for_all.index('C'))

# Exercise 21
print(c_for_all.index('F'))

# Exercise 22
print('Coding For All People'.rfind('l'))

# Exercise 23
print('You cannot end a sentence with because because because is a conjunction'.find('because'))

# Exercise 24
print('You cannot end a sentence with because because because is a conjunction'.rfind('because'))

# Exercise 25
phrase = 'You cannot end a sentence with because because because is a conjunction'
start = phrase.find('because')
end = phrase.rfind('because') + len('because')

print(phrase[start: end])

# Exercise 26
print('You cannot end a sentence with because because because is a conjunction'.find('because'))

# Exercise 27
print(phrase[start: end])

# Exercise 28
print('Coding For All'.startswith('Coding'))

# Exercise 29
print('Coding For All'.endswith('coding'))

# Exercise 30
print('   Coding For All      '.strip())

# Exercise 31
print('thirty_days_of_python'.isidentifier())

# Exercise 32
print(' # '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

# Exercise 33
print("I am enjoying this challenge.\nI just wonder what is next.")

# Exercise 34
print("Name\t\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# Exercise 35
radius = 10
area = 3.14 * radius ** 2
print(f'radius = {radius}')
print(f'The area of a circle with radius {radius} is {area} meters square.')

# Exercise 36
n1 = 8
n2 = 6

print(f'{n1} + {n2} = {n1 + n2}')
print(f'{n1} - {n2} = {n1 - n2}')
print(f'{n1} * {n2} = {n1 * n2}')
print(f'{n1} / {n2} = {n1 / n2:.2f}')
print(f'{n1} % {n2} = {n1 % n2}')
print(f'{n1} // {n2} = {n1 // n2}')
print(f'{n1} ** {n2} = {n1 ** n2}')