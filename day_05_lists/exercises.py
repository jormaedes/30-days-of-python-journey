# =============================================================
# Day 5 - Lists | 30 Days of Python
# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/05_lists.md
# =============================================================


# --- Level 1 ---

# 1. Declarar uma lista vazia
empty_list = []
print(empty_list)        # []
print(type(empty_list))  # <class 'list'>

# 2. Declarar uma lista com mais de 5 itens
my_list = [1, 2, 3, 4, 5, 6, 7]
print(my_list)

# 3. Comprimento da lista
print(len(my_list))  # 7

# 4. Primeiro, do meio e último item da lista
print(my_list[0])               # 1  — primeiro
print(my_list[len(my_list)//2]) # 4  — do meio
print(my_list[-1])              # 7  — último

# 5. Declarar a lista it_companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 6. Imprimir a lista e número de empresas
print(it_companies)
print('Number of companies:', len(it_companies))  # 7

# 7. Primeira, do meio e última empresa
print(it_companies[0])                     # Facebook
print(it_companies[len(it_companies)//2])  # Apple
print(it_companies[-1])                    # Amazon

# 8. Modificar uma empresa
it_companies[0] = 'Meta'  # Facebook → Meta
print(it_companies)

# 9. Adicionar uma empresa
it_companies.append('Netflix')
print(it_companies)

# 10. Inserir uma empresa no meio da lista
mid = len(it_companies) // 2
it_companies.insert(mid, 'Tesla')
print(it_companies)

# 11. Mudar o nome de uma das empresas para maiúsculas
it_companies[1] = it_companies[1].upper()  # GOOGLE
print(it_companies)

# 12. Juntar it_companies com ' # '
print(' # '.join(it_companies))

# 13. Verificar se uma empresa existe na lista
print('Apple' in it_companies)    # True
print('Twitter' in it_companies)  # False

# 14. Ordenar a lista com o método sort()
it_companies.sort()
print(it_companies)

# 15. Ordenar em ordem inversa com o método sort() e reverse=True
it_companies.sort(reverse=True)
print(it_companies)

# 16. Reverter a lista com o método reverse()
it_companies.reverse()
print(it_companies)

# 17. Fatiar as primeiras 3 empresas
print(it_companies[:3])

# 18. Fatiar as últimas 3 empresas
print(it_companies[-3:])

# 19. Fatiar a(s) empresa(s) do meio
mid = len(it_companies) // 2
print(it_companies[mid - 1 : mid + 1])

# 20. Remover a primeira empresa da lista
it_companies.pop(0)
print(it_companies)

# 21. Remover a empresa do meio da lista
mid = len(it_companies) // 2
it_companies.pop(mid)
print(it_companies)

# 22. Remover a última empresa da lista
it_companies.pop()
print(it_companies)

# 23. Remover todas as empresas
it_companies.clear()
print(it_companies)  # []


# --- Level 2 ---

# Listas base para os exercícios do nível 2
fruits          = ['banana', 'orange', 'mango', 'lemon']
vegetables      = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
animal_products = ['milk', 'meat', 'butter', 'yoghurt']
web_technologies = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']
countries       = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# 24. Imprimir cada lista e o número de itens
print(f"Fruits: {fruits}")
print(f"Number of fruits: {len(fruits)}")

print(f"Vegetables: {vegetables}")
print(f"Number of vegetables: {len(vegetables)}")

print(f"Animal products: {animal_products}")
print(f"Number of animal products: {len(animal_products)}")

print(f"Web technologies: {web_technologies}")
print(f"Number of web technologies: {len(web_technologies)}")

print(f"Countries: {countries}")
print(f"Number of countries: {len(countries)}")

# 25. Juntar fruits e vegetables e guardá-la na variável food_stuff_tp
food_stuff_tp = fruits + vegetables
print(food_stuff_tp)

# 26. Converter food_stuff_tp numa tupla
food_stuff_tp = tuple(food_stuff_tp)
print(food_stuff_tp)
print(type(food_stuff_tp))  # <class 'tuple'>

# 27. Criar food_stuff_st a partir de food_stuff_tp e removendo duplicados (conjunto)
food_stuff_st = set(food_stuff_tp)
print(food_stuff_st)
print(type(food_stuff_st))  # <class 'set'>

# 28. Fatiar food_stuff_st → primeiros 3 e últimos 3 (converter para lista primeiro)
food_list = list(food_stuff_tp)
print(food_list[:3])   # primeiros 3
print(food_list[-3:])  # últimos 3

# 29. Apagar food_stuff_tp e food_stuff_st
del food_stuff_tp
del food_stuff_st

# 30. Juntar animal_products e web_technologies
it_stuff = animal_products + web_technologies
print(it_stuff)


# --- Level 3 ---

# 31. Copiar it_stuff para full_stack, depois inserir Python e SQL depois de Redux
full_stack = it_stuff.copy()
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')
print(full_stack)

# 32. Dividir a lista countries em duas metades iguais.
# Se o número for ímpar, a primeira metade fica com o elemento a mais.
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
mid = (len(countries) + 1) // 2      # arredonda para cima se ímpar
first_half  = countries[:mid]
second_half = countries[mid:]
print('First half:', first_half)     # ['Finland', 'Estonia', 'Denmark']
print('Second half:', second_half)   # ['Sweden', 'Norway']

# 33. Desempacotar as primeiras 3 frutas e guardar o resto numa variável chamada other_fruits
first_fruit, second_fruit, third_fruit, *other_fruits = fruits
print(first_fruit)    # banana
print(second_fruit)   # orange
print(third_fruit)    # mango
print(other_fruits)   # ['lemon']