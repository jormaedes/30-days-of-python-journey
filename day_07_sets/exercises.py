# =============================================================
# Day 7 - Sets | 30 Days of Python
# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/07_Day_Sets/07_sets.md
# =============================================================

# Sets base fornecidos pelo curso
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A   = {19, 22, 24, 20, 25, 26}
B   = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# --- Level 1 ---

# 1. Comprimento de it_companies
print(len(it_companies))  # 7

# 2. Adicionar 'Twitter' a it_companies
it_companies.add('Twitter')
print(it_companies)

# 3. Inserir múltiplas empresas de uma vez
it_companies.update(['Netflix', 'Tesla', 'Spotify'])
print(it_companies)

# 4. Remover uma empresa do set
it_companies.remove('IBM')
print(it_companies)

# 5. Diferença entre remove() e discard()
# .remove(x) → lança KeyError se o elemento não existir no set
# .discard(x) → não faz nada e não lança qualquer erro se o elemento não existir
# Exemplo prático:
it_companies.discard('IBM')   # IBM já foi removido — sem erro ✅
# it_companies.remove('IBM')  # IBM já foi removido — KeyError ❌


# --- Level 2 ---

# 1. Juntar A e B (união)
print(A.union(B))  # método
print(A | B)       # operador equivalente

# 2. Intersecção de A e B
print(A.intersection(B))  # método
print(A & B)              # operador equivalente

# 3. A é subconjunto de B?
# A = {19, 20, 22, 24, 25, 26}
# B = {19, 20, 22, 24, 25, 26, 27, 28}
# Todos os elementos de A existem em B → True
print(A.issubset(B))  # True
print(A <= B)         # True

# 4. A e B são disjuntos (sem elementos em comum)?
print(A.isdisjoint(B))  # False — partilham vários elementos

# 5. Juntar A com B e B com A (usando update — modifica o original)
A_copy = A.copy()
B_copy = B.copy()

A_copy.update(B)
print(f'A unido com B: {A_copy}')

B_copy.update(A)
print(f'B unido com A: {B_copy}')
# A união é comutativa — A|B == B|A

# 6. Diferença simétrica entre A e B
# Elementos que estão em A ou em B, mas NÃO em ambos → {27, 28}
print(A.symmetric_difference(B))  # método
print(A ^ B)                      # operador

# 7. Apagar os sets completamente
del A_copy
del B_copy


# --- Level 3 ---

# 1. Converter a lista age para set e comparar os tamanhos
print(f'Lista age:          {age}')
print(f'Comprimento lista:  {len(age)}')     # 8 — com duplicados

age_set = set(age)
print(f'Set age:            {age_set}')
print(f'Comprimento set:    {len(age_set)}') # 5 — sem duplicados
print(f'Duplicados removidos: {len(age) - len(age_set)}')

# 2. Explicar as diferenças entre: string, list, tuple e set
"""
COMPARAÇÃO ENTRE TIPOS DE DADOS:

| Tipo   | Ordenado | Indexável | Mutável | Duplicados | Exemplo         |
|--------|----------|-----------|---------|------------|-----------------|
| str    |    ✅    |    ✅     |   ❌   |     ✅     | 'Python'        |
| list   |    ✅    |    ✅     |   ✅   |     ✅     | [1, 2, 2, 3]    |
| tuple  |    ✅    |    ✅     |   ❌   |     ✅     | (1, 2, 2, 3)    |
| set    |    ❌    |    ❌     |   ✅   |     ❌     | {1, 2, 3}       |

- string : sequência imutável de caracteres — ideal para texto
- list   : sequência mutável e ordenada — ideal para dados que mudam
- tuple  : como list mas imutável — ideal para dados fixos/constantes
- set    : colecção não ordenada de elementos únicos — ideal para operações matemáticas
           e para remover duplicados
"""

# 3. Contar palavras únicas na frase
sentence     = 'I am a teacher and I love to inspire and teach people'
words        = sentence.split()
unique_words = set(words)

print(f'Frase:               "{sentence}"')
print(f'Total de palavras:    {len(words)}')        # 11
print(f'Palavras únicas:      {len(unique_words)}') # 9 (I e and repetem-se)
print(f'Palavras únicas:      {unique_words}')