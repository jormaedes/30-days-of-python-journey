# =============================================================
# Day 6 - Tuples | 30 Days of Python
# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/06_Day_Tuples/06_tuples.md
# =============================================================


# --- Level 1 ---

# 1. Criar uma tuple vazia
empty_tuple = ()
print(empty_tuple)        # ()
print(type(empty_tuple))  # <class 'tuple'>

# 2. Criar tuples com nomes de irmãs e irmãos
sisters  = ('Jaribaby', 'Rebeca')
brothers = ('Diloy', 'Dalmir')
print(sisters)
print(brothers)

# 3. Juntar as duas tuples e atribuir a siblings
siblings = sisters + brothers
print(siblings)  # ('Ana', 'Sofia', 'Miguel', 'João')

# 4. Quantos irmãos tens?
print(f'Tenho {len(siblings)} irmãos.')  # 4

# 5. Modificar siblings para adicionar o nome do pai e da mãe
#    Como tuples são imutáveis, converter para lista, modificar, e converter de volta
siblings = list(siblings)
siblings.insert(0, 'Pai Jorge')   # adicionar o pai
siblings.insert(1, 'Mãe Maria')     # adicionar a mãe
family_members = tuple(siblings)
print(family_members)
# ('Pai António', 'Mãe Maria', 'Ana', 'Sofia', 'Miguel', 'João')


# --- Level 2 ---

# 1. Desempacotar siblings e parents a partir de family_members
parents = family_members[:2]   # ('Pai António', 'Mãe Maria')
siblings = family_members[2:]  # ('Ana', 'Sofia', 'Miguel', 'João')
print(f'Parents: {parents}')
print(f'Siblings: {siblings}')

# 2. Criar tuples de frutas, vegetais e produtos animais e juntá-las em food_stuff_tp
fruits          = ('banana', 'orange', 'mango', 'lemon')
vegetables      = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
animal_products = ('milk', 'meat', 'butter', 'yoghurt')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
print(f'Total items: {len(food_stuff_tp)}')  # 13

# 3. Converter food_stuff_tp para uma lista food_stuff_lt
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
print(type(food_stuff_lt))  # <class 'list'>

# 4. Fatiar o(s) item(s) do meio de food_stuff_lt
mid = len(food_stuff_lt) // 2
# Se o comprimento for ímpar, o meio é um único elemento
if len(food_stuff_lt) % 2 == 0:
    middle = food_stuff_lt[mid - 1 : mid + 1]  # dois elementos do meio
else:
    middle = food_stuff_lt[mid]                 # elemento central
print(f'Middle item(s): {middle}')

# 5. Fatiar os primeiros 3 e os últimos 3 de food_stuff_lt
print(f'First three: {food_stuff_lt[:3]}')   # ['banana', 'orange', 'mango']
print(f'Last three:  {food_stuff_lt[-3:]}')  # ['milk', 'meat', 'butter', 'yoghurt'][-3:]

# 6. Apagar food_stuff_tp completamente
del food_stuff_tp
# print(food_stuff_tp)  # ← NameError se descomentar: nome já não existe

# 7. Verificar se um item existe na tuple nordic_countries
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)  # False — Estónia não é país nórdico
print('Iceland' in nordic_countries)  # True  — Islândia é país nórdico

# Mensagens mais descritivas
country = 'Estonia'
if country in nordic_countries:
    print(f'{country} is a nordic country.')
else:
    print(f'{country} is not a nordic country.')

country = 'Iceland'
if country in nordic_countries:
    print(f'{country} is a nordic country.')
else:
    print(f'{country} is not a nordic country.')