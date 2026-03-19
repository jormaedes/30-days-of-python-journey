# 📘 Dia 7 — Sets

📖 **Conteúdo do curso:** [Day 7 - Sets](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/07_Day_Sets/07_sets.md)
💻 **Exercícios resolvidos:** [exercises.py](./exercises.py)

---

## ✏️ O que aprendi hoje

O dia 7 apresenta a estrutura de dados mais matemática do Python. Um set é uma **colecção não ordenada de elementos únicos** — exactamente como os conjuntos da matemática do ensino secundário. A grande vantagem dos sets é que removem duplicados automaticamente e permitem operações matemáticas entre conjuntos de forma muito eficiente.

---

## 1. Criar um Set

```python
# Set vazio — ATENÇÃO: {} cria um dicionário, não um set!
empty_set  = set()  # ✅ set vazio
empty_dict = {}     # ❌ isto é um dicionário

# Set com valores
frutas  = {'banana', 'laranja', 'manga', 'limão'}
numeros = {1, 2, 3, 4, 5}

# Duplicados são removidos automaticamente!
st = {1, 2, 2, 3, 3, 3}
print(st)  # {1, 2, 3}
```

> ⚠️ Como os sets são **não ordenados**, a ordem dos elementos no output pode variar. Não podes usar índices — não existe `st[0]`.

---

## 2. Comprimento

```python
frutas = {'banana', 'laranja', 'manga', 'limão'}
print(len(frutas))  # 4
```

---

## 3. Verificar se um item existe

```python
frutas = {'banana', 'laranja', 'manga'}
print('manga' in frutas)   # True
print('uva' in frutas)     # False
```

---

## 4. Adicionar elementos

```python
frutas = {'banana', 'laranja', 'manga'}

frutas.add('limão')              # adiciona um elemento
frutas.update(['uva', 'kiwi'])   # adiciona múltiplos (aceita lista, tuple ou set)
print(frutas)
```

---

## 5. Remover elementos

```python
frutas = {'banana', 'laranja', 'manga', 'limão'}

frutas.remove('manga')  # lança KeyError se o elemento não existir ❌
frutas.discard('uva')   # NÃO lança erro se o elemento não existir ✅
frutas.pop()            # remove um elemento aleatório (set não é ordenado!)
frutas.clear()          # esvazia o set → set()
del frutas              # apaga o set completamente da memória
```

> 💡 **`remove` vs `discard`** — a diferença chave:
> - `.remove(x)` → lança `KeyError` se `x` não existir
> - `.discard(x)` → não faz nada se `x` não existir (mais seguro)

---

## 6. Converter Lista para Set — remover duplicados

Um dos usos mais práticos no dia-a-dia:

```python
idades = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(idades))         # 8  — com duplicados

idades_unicas = set(idades)
print(idades_unicas)        # {19, 22, 24, 25, 26}
print(len(idades_unicas))   # 5  — sem duplicados

# Padrão clássico: remover duplicados de uma lista
lista_limpa = list(set(idades))
```

---

## 7. Operações entre Sets ⭐

A parte mais poderosa do dia. Cada operação tem um **método** e um **operador** equivalente:

### União — todos os elementos de ambos

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))  # {1, 2, 3, 4, 5, 6}
print(A | B)       # {1, 2, 3, 4, 5, 6}
```

### Intersecção — apenas os elementos comuns

```python
print(A.intersection(B))  # {3, 4}
print(A & B)              # {3, 4}
```

### Diferença — elementos de A que não estão em B

```python
print(A.difference(B))  # {1, 2}  ← a ordem importa!
print(A - B)            # {1, 2}

print(B.difference(A))  # {5, 6}  ← resultado diferente
print(B - A)            # {5, 6}
```

### Diferença Simétrica — num OU noutro, mas não em ambos

```python
print(A.symmetric_difference(B))  # {1, 2, 5, 6}
print(A ^ B)                      # {1, 2, 5, 6}
```

---

## 8. Subset, Superset e Disjoint

```python
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

print(A.issubset(B))    # True  — todos os elementos de A estão em B
print(A <= B)           # True  — operador equivalente

print(B.issuperset(A))  # True  — B contém todos os elementos de A
print(B >= A)           # True

pares   = {0, 2, 4, 6, 8}
impares = {1, 3, 5, 7, 9}
print(pares.isdisjoint(impares))  # True — zero elementos em comum
```

---

## 9. Resumo de operações — tabela rápida

| Operação | Método | Operador | O que devolve |
|---|---|---|---|
| União | `.union(B)` | `A \| B` | Todos os elementos de A e B |
| Intersecção | `.intersection(B)` | `A & B` | Só os elementos comuns |
| Diferença | `.difference(B)` | `A - B` | Em A mas não em B |
| Dif. Simétrica | `.symmetric_difference(B)` | `A ^ B` | Num ou noutro, mas não em ambos |
| Subset | `.issubset(B)` | `A <= B` | `True` se A ⊆ B |
| Superset | `.issuperset(B)` | `A >= B` | `True` se A ⊇ B |
| Disjoint | `.isdisjoint(B)` | — | `True` se não partilham elementos |

---

## 10. Sets vs Listas vs Tuples

| | Lista `[]` | Tuple `()` | Set `{}` |
|---|---|---|---|
| Ordenada | ✅ | ✅ | ❌ |
| Indexável | ✅ | ✅ | ❌ |
| Mutável | ✅ | ❌ | ✅ |
| Permite duplicados | ✅ | ✅ | ❌ |
| Operações matemáticas | ❌ | ❌ | ✅ |

---

## 💡 Conceitos que achei interessantes

- `{}` vazio é sempre um **dicionário** — para set vazio tens obrigatoriamente de usar `set()`
- Como sets não são ordenados, `.pop()` remove um elemento **aleatório**, ao contrário das listas onde remove o último
- A diferença simétrica `^` é como um XOR: só o que pertence a exactamente um dos sets
- `list(set(lista))` é o atalho mais rápido para remover duplicados de uma lista em Python

---

## ⚠️ Armadilhas comuns

```python
# 1. {} vazio não é um set!
x = {}
print(type(x))   # <class 'dict'>  ← armadilha!
x = set()
print(type(x))   # <class 'set'>   ← correcto

# 2. Sets não suportam indexação
frutas = {'banana', 'laranja'}
print(frutas[0])  # ❌ TypeError: 'set' object is not subscriptable

# 3. A ordem da diferença importa
A, B = {1, 2, 3}, {3, 4, 5}
print(A - B)  # {1, 2}
print(B - A)  # {4, 5}  ← resultado completamente diferente!
```
