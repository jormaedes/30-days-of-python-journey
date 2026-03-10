# 📘 Dia 6 — Tuples

📖 **Conteúdo do curso:** [Day 6 - Tuples](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/06_Day_Tuples/06_tuples.md)
💻 **Exercícios resolvidos:** [exercises.py](./exercises.py)

---

## ✏️ O que aprendi hoje

O dia 6 é mais curto do que o dia 5. As tuplas são basicamente **listas imutáveis**: a sintaxe é quase idêntica, mas depois de criadas não podes alterar, adicionar ou remover elementos. Têm menos métodos exactamente porque fazem menos coisas.

A grande questão do dia é perceber: **quando usar tupla em vez de lista?**

---

## 1. O que é uma Tuple?

Uma tuple é uma colecção **ordenada** e **imutável** de elementos. É escrita com parênteses `()`.

```python
# Tuple vazia
empty_tuple = ()
empty_tuple = tuple()

# Tuple com valores
numeros    = (1, 2, 3)
misturada  = ('João', 25, True, 1.80)   # tipos diferentes
aninhada   = ('Python', (1, 2, 3))      # tuple dentro de tuple
```

> ⚠️ **Tuple com um único elemento** — tens de por uma vírgula no final, caso contrário Python interpreta os parênteses como agrupamento matemático:
> ```python
> nao_e_tuple = (5)     # int → type: <class 'int'>
> e_tuple     = (5,)    # tuple → type: <class 'tuple'>
> ```

---

## 2. Comprimento

```python
tpl = ('item1', 'item2', 'item3')
print(len(tpl))  # 3
```

---

## 3. Indexação e Slicing

Funciona exactamente igual às listas e strings — mesma lógica, mesma sintaxe:

```python
frutas = ('banana', 'laranja', 'manga', 'limão')
#          [0]        [1]       [2]      [3]
#          [-4]       [-3]      [-2]     [-1]

print(frutas[0])    # banana
print(frutas[-1])   # limão
print(frutas[1:3])  # ('laranja', 'manga')
print(frutas[::-1]) # ('limão', 'manga', 'laranja', 'banana')
```

---

## 4. Os únicos dois métodos das Tuples

Ao contrário das listas, as tuples **só têm 2 métodos**:

```python
numeros = (1, 2, 3, 2, 4, 2)

print(numeros.count(2))   # 3  — conta quantas vezes o valor 2 aparece
print(numeros.index(3))   # 2  — devolve o índice da primeira ocorrência de 3
```

Não existem `.append()`, `.remove()`, `.sort()`, etc. — porque a tuple é imutável.

---

## 5. Verificar se um elemento existe

```python
frutas = ('banana', 'laranja', 'manga')

print('manga' in frutas)     # True
print('uva' in frutas)       # False
print('uva' not in frutas)   # True
```

---

## 6. Juntar Tuples

```python
frutas     = ('banana', 'laranja', 'manga')
vegetais   = ('tomate', 'cenoura', 'cebola')

comida = frutas + vegetais
print(comida)
# ('banana', 'laranja', 'manga', 'tomate', 'cenoura', 'cebola')
```

---

## 7. Apagar uma Tuple

Não podes apagar um elemento individual (imutável), mas podes apagar a tuple inteira:

```python
tpl = (1, 2, 3)
del tpl
print(tpl)  # NameError: name 'tpl' is not defined
```

---

## 8. Converter entre Tuple e Lista ⭐

Esta é a técnica mais importante do dia: quando precisares de **modificar** uma tuple, convertes para lista, modificas, e convertes de volta.

```python
frutas = ('banana', 'laranja', 'manga', 'limão')

# Converter para lista → modificar → converter de volta
frutas = list(frutas)        # tuple → list
frutas[0] = 'abacate'        # modificar
frutas.append('uva')         # adicionar
frutas = tuple(frutas)       # list → tuple

print(frutas)
# ('abacate', 'laranja', 'manga', 'limão', 'uva')
```

---

## 9. Unpacking de Tuples

Funciona igual ao das listas, incluindo o operador `*`:

```python
# Unpacking simples
primeiro, segundo, terceiro = ('banana', 'laranja', 'manga')
print(primeiro)   # banana

# Com * para capturar o resto
primeiro, *resto = ('banana', 'laranja', 'manga', 'limão')
print(primeiro)   # banana
print(resto)      # ['laranja', 'manga', 'limão']  ← devolve uma lista!
```

> 💡 Nota: o `*resto` devolve sempre uma **lista**, mesmo que a tuple original seja de outro tipo.

---

## 10. Tuple vs Lista — quando usar cada uma?

| Característica | Lista `[]` | Tuple `()` |
|---|---|---|
| Mutável | ✅ Sim | ❌ Não |
| Métodos disponíveis | Muitos | Apenas 2 |
| Performance | Mais lenta | Mais rápida |
| Uso de memória | Mais | Menos |
| Quando usar | Dados que vão mudar | Dados fixos/constantes |

**Exemplos práticos de quando usar tuples:**

```python
# Coordenadas geográficas (não mudam)
luanda = (-8.8368, 13.2343)

# Retornar múltiplos valores de uma função (veremos no dia 11)
def min_max(lst):
    return (min(lst), max(lst))

# Como chaves de dicionário (listas não podem ser chaves)
localizacoes = {(-8.8368, 13.2343): 'Luanda'}
```

---

## 💡 Conceitos que achei interessantes

- A tupla com um único elemento precisa de vírgula — `(5,)` e não `(5)` — é uma armadilha clássica
- O `*` no unpacking devolve sempre uma lista, independentemente do tipo original
- Tuples podem ser usadas como **chaves de dicionário** (dia 8), mas listas não — porque as listas são mutáveis e não são "hashable"
- A imutabilidade não é uma limitação, é uma garantia: quando passas uma tuple para uma função, tens a certeza de que ela não vai ser alterada

---

## ⚠️ Armadilhas comuns

```python
# 1. Tentar modificar directamente → erro
tpl = (1, 2, 3)
tpl[0] = 10  # ❌ TypeError: 'tuple' object does not support item assignment

# 2. Tuple de um elemento sem vírgula
t = (5)
print(type(t))   # ❌ <class 'int'> — não é tuple!
t = (5,)
print(type(t))   # ✅ <class 'tuple'>

# 3. Confundir tuple vazia com parênteses
t = ()           # ✅ tuple vazia
t = tuple()      # ✅ também tuple vazia
```

