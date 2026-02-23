# 📘 Dia 5 — Lists

📖 **Conteúdo do curso:** [Day 5 - Lists](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/05_lists.md)
💻 **Exercícios resolvidos:** [exercises.py](./exercises.py)

---

## ✏️ O que aprendi hoje

As listas são a estrutura de dados mais usada em Python. Ao contrário das strings (imutáveis), as listas são **mutáveis** — podes alterar, adicionar e remover elementos depois de as criar. Podem guardar qualquer tipo de dado, inclusive tipos misturados.

---

## 1. Criar uma lista

```python
# Lista vazia
lista_vazia = []
lista_vazia = list()

# Listas com valores
frutas     = ['banana', 'laranja', 'manga', 'limão']
numeros    = [1, 2, 3, 4, 5]
misturada  = ['João', 25, True, 1.80]              # tipos diferentes
aninhada   = ['Python', [1, 2, 3], {'chave': 'valor'}]  # lista dentro de lista
```

---

## 2. Indexação — aceder a elementos

```python
frutas = ['banana', 'laranja', 'manga', 'limão']
#          [0]        [1]       [2]      [3]
#          [-4]       [-3]      [-2]     [-1]

print(frutas[0])   # 'banana'  — primeiro elemento
print(frutas[-1])  # 'limão'   — último elemento
print(frutas[-2])  # 'manga'

# Listas aninhadas
matriz = [[1, 2, 3], [4, 5, 6]]
print(matriz[0][1])  # 2
```

---

## 3. Unpacking — desempacotar

```python
primeiro, segundo, terceiro = ['banana', 'laranja', 'manga']
print(primeiro)   # banana
print(segundo)    # laranja
print(terceiro)   # manga

# Com * para capturar o resto
primeiro, *resto = ['banana', 'laranja', 'manga', 'limão']
print(primeiro)  # banana
print(resto)     # ['laranja', 'manga', 'limão']
```

---

## 4. Slicing — fatiar a lista

```python
frutas = ['banana', 'laranja', 'manga', 'limão', 'uva']

print(frutas[1:3])    # ['laranja', 'manga']   — índice 1 ao 2
print(frutas[::2])    # ['banana', 'manga', 'uva']  — de 2 em 2
print(frutas[::-1])   # ['uva', 'limão', 'manga', 'laranja', 'banana']  — invertida
print(frutas[:3])     # ['banana', 'laranja', 'manga']  — do início ao índice 2
print(frutas[2:])     # ['manga', 'limão', 'uva']   — do índice 2 ao fim
```

---

## 5. Modificar elementos

As listas são **mutáveis** — podes alterar qualquer elemento pelo índice:

```python
frutas = ['banana', 'laranja', 'manga']
frutas[0] = 'abacate'
print(frutas)  # ['abacate', 'laranja', 'manga']
```

---

## 6. Verificar se um item existe

```python
frutas = ['banana', 'laranja', 'manga']
print('manga' in frutas)     # True
print('uva' in frutas)       # False
print('uva' not in frutas)   # True
```

---

## 7. Métodos de listas

### Adicionar elementos

```python
frutas = ['banana', 'laranja']

frutas.append('manga')           # adiciona no fim
print(frutas)  # ['banana', 'laranja', 'manga']

frutas.insert(1, 'uva')          # insere na posição 1
print(frutas)  # ['banana', 'uva', 'laranja', 'manga']

frutas.extend(['limão', 'kiwi']) # junta outra lista no fim
print(frutas)  # ['banana', 'uva', 'laranja', 'manga', 'limão', 'kiwi']
```

### Remover elementos

```python
frutas = ['banana', 'laranja', 'manga', 'laranja']

frutas.remove('laranja')  # remove a PRIMEIRA ocorrência
print(frutas)  # ['banana', 'manga', 'laranja']

ultimo = frutas.pop()     # remove e devolve o último elemento
print(ultimo)  # 'laranja'

segundo = frutas.pop(1)   # remove e devolve o elemento no índice 1
print(segundo) # 'manga'

del frutas[0]             # apaga o elemento no índice 0
del frutas[0:2]           # apaga um intervalo

frutas.clear()            # esvazia a lista completamente → []
```

> ⚠️ **Diferença importante:**
> - `.remove(valor)` → procura pelo **valor**
> - `.pop(índice)` → procura pelo **índice**, e **devolve** o elemento removido
> - `del lista[índice]` → apaga pelo **índice**, mas **não devolve** nada

### Copiar uma lista

```python
frutas = ['banana', 'laranja', 'manga']

# ❌ Errado — cria apenas uma referência, não uma cópia
copia_errada = frutas
copia_errada[0] = 'uva'
print(frutas)  # ['uva', 'laranja', 'manga'] — o original mudou!

# ✅ Correto — cria uma cópia independente
copia_certa = frutas.copy()
copia_certa[0] = 'uva'
print(frutas)  # ['banana', 'laranja', 'manga'] — o original intacto
```

### Juntar listas

```python
front_end = ['HTML', 'CSS', 'JS']
back_end  = ['Node', 'Express', 'MongoDB']

# Forma 1: operador +
full_stack = front_end + back_end

# Forma 2: extend()
front_end.extend(back_end)
```

### Outros métodos úteis

```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6]

print(len(numeros))        # 8   — comprimento
print(numeros.count(1))    # 2   — quantas vezes aparece o valor 1
print(numeros.index(5))    # 4   — índice da primeira ocorrência de 5

numeros.reverse()          # inverte a lista NO LUGAR (modifica o original)
print(numeros)             # [6, 2, 9, 5, 1, 4, 1, 3]

numeros.sort()             # ordena crescente NO LUGAR
print(numeros)             # [1, 1, 2, 3, 4, 5, 6, 9]

numeros.sort(reverse=True) # ordena decrescente
print(numeros)             # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() — devolve uma nova lista sem modificar o original
frutas = ['manga', 'banana', 'limão']
print(sorted(frutas))              # ['banana', 'limão', 'manga']
print(sorted(frutas, reverse=True))# ['manga', 'limão', 'banana']
print(frutas)                      # ['manga', 'banana', 'limão'] — intacto
```

---

## 8. Resumo de métodos — tabela rápida

| Método | O que faz | Modifica o original? |
|---|---|---|
| `.append(x)` | Adiciona `x` no fim | ✅ Sim |
| `.insert(i, x)` | Insere `x` na posição `i` | ✅ Sim |
| `.extend(lst)` | Junta outra lista no fim | ✅ Sim |
| `.remove(x)` | Remove a 1ª ocorrência de `x` | ✅ Sim |
| `.pop(i)` | Remove e devolve o elemento em `i` | ✅ Sim |
| `.clear()` | Esvazia a lista | ✅ Sim |
| `.sort()` | Ordena a lista | ✅ Sim |
| `.reverse()` | Inverte a lista | ✅ Sim |
| `.copy()` | Devolve uma cópia independente | ❌ Não |
| `.count(x)` | Conta ocorrências de `x` | ❌ Não |
| `.index(x)` | Devolve o índice de `x` | ❌ Não |
| `sorted(lst)` | Devolve nova lista ordenada | ❌ Não |
| `len(lst)` | Devolve o comprimento | ❌ Não |

---

## 💡 Conceitos que achei interessantes

- A diferença entre `.sort()` e `sorted()` é subtil mas importante — `.sort()` modifica a lista original e não devolve nada útil, enquanto `sorted()` cria uma nova lista e deixa o original intacto
- Fazer `copia = lista` **não cria uma cópia** — cria dois nomes a apontar para o mesmo objeto em memória. Sempre usar `.copy()` quando precisares de uma cópia independente
- O unpacking com `*` é muito prático para separar o primeiro elemento do resto

---

## ⚠️ Armadilhas comuns

```python
# 1. Modificar uma lista enquanto se itera sobre ela → comportamento imprevisível
#    (veremos como iterar no dia 10 - Loops)

# 2. Cópia por referência — já visto acima

# 3. .sort() não devolve a lista — devolve None
frutas = ['manga', 'banana']
resultado = frutas.sort()
print(resultado)  # None ← armadilha!
print(frutas)     # ['banana', 'manga'] ← a lista foi alterada
```
