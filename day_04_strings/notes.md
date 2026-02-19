# 📘 Dia 4 — Strings

📖 **Conteúdo do curso:** [Day 4 - Strings](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/04_Day_Strings/04_strings.md)
💻 **Exercícios resolvidos:** [exercises.py](./exercises.py)

---

## ✏️ O que aprendi hoje

O dia 4 é um dos mais densos do curso — strings em Python têm muita coisa. O essencial é perceber que uma string é uma **sequência de caracteres imutável**, (diferente do C/C++) o que significa que não podes alterar um caractere diretamente; tens sempre de criar uma nova string.

---

## 1. Criar strings

```python
letra       = 'P'
frase       = "Hello, World!"
multilinha  = '''Isto é
uma string
com várias linhas.'''
```

- Podes usar aspas simples `'` ou duplas `"` — o resultado é o mesmo
- Para strings com mais de uma linha usa aspas triplas `'''` ou `"""`

---

## 2. Concatenação e comprimento

```python
primeiro_nome = 'João'
ultimo_nome   = 'Silva'
nome_completo = primeiro_nome + ' ' + ultimo_nome  # concatenação com +

print(len(nome_completo))  # 10 — len() devolve o número de caracteres
```

---

## 3. Escape sequences (caracteres especiais)

| Sequência | Significado         |
|-----------|---------------------|
| `\n`      | Nova linha          |
| `\t`      | Tabulação (tab)     |
| `\\`      | Barra invertida `\` |
| `\"`      | Aspas duplas        |
| `\'`      | Aspas simples       |

```python
print('Linha 1\nLinha 2')       # quebra de linha
print('Nome\tIdade\tPaís')      # tab entre colunas
print('Símbolo de barra: \\')   # imprime \
```

---

## 4. Formatação de strings

Existem 3 formas de formatar strings em Python:

### 4.1 Operador `%` (antigo)
```python
nome = 'Jormaedes'
print('Olá, %s!' % nome)
```

### 4.2 Método `.format()`
```python
a, b = 4, 3
print('{} + {} = {}'.format(a, b, a + b))
print('{} / {} = {:.2f}'.format(a, b, a / b))  # 2 casas decimais
```

### 4.3 f-strings ⭐ (forma moderna e recomendada)
```python
nome  = 'Jormaedes'
idade = 25
print(f'Olá, {nome}! Tens {idade} anos.')

radius = 10
area   = 3.14 * radius ** 2
print(f'A área do círculo com raio {radius} é {area:.2f} m²')
```
> 💡 **Usar sempre f-strings** — são mais legíveis e mais rápidas.

---

## 5. Indexação e slicing

Strings são sequências, por isso podes aceder a cada caractere pelo seu índice (começa em 0).

```python
linguagem = 'Python'
#            P  y  t  h  o  n
# índice:    0  1  2  3  4  5
# negativo: -6 -5 -4 -3 -2 -1

print(linguagem[0])   # P
print(linguagem[-1])  # n  (último caractere)
```

### Slicing — `[inicio:fim:passo]`

```python
print(linguagem[0:3])   # Pyt  (do índice 0 ao 2, o 3 não é incluído)
print(linguagem[::1])   # Python (string completa)
print(linguagem[::-1])  # nohtyP (string invertida!)
```

---

## 6. Métodos de strings mais importantes

Strings têm dezenas de métodos built-in. Os essenciais do dia 4:

```python
s = '  Coding For All  '

# Maiúsculas / minúsculas
print(s.upper())         # '  CODING FOR ALL  '
print(s.lower())         # '  coding for all  '
print(s.capitalize())    # '  coding for all  ' → só 1ª letra maiúscula
print(s.title())         # '  Coding For All  '
print(s.swapcase())      # inverte maiúsculas e minúsculas

# Espaços
print(s.strip())         # 'Coding For All'  → remove espaços dos dois lados
print(s.lstrip())        # 'Coding For All  ' → só esquerda
print(s.rstrip())        # '  Coding For All' → só direita

# Pesquisa
print(s.startswith('  Cod'))    # True
print(s.endswith('All  '))      # True
print(s.find('For'))            # 9  → índice onde começa (ou -1 se não existir)
print(s.index('For'))           # 9  → igual ao find mas lança erro se não existir
print(s.count('o'))             # 2

# Substituição e divisão
print(s.replace('Coding', 'Python'))   # '  Python For All  '
print(s.strip().split(' '))            # ['Coding', 'For', 'All']

# Verificações (devolvem True ou False)
print('Python3'.isidentifier())  # True
print('123'.isdigit())           # True
print('abc'.isalpha())           # True
print('abc123'.isalnum())        # True

# Juntar uma lista numa string
libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libs))  # Django # Flask # Bottle # Pyramid # Falcon
```

---

## 💡 Conceitos que achei interessantes

- O slicing `[::-1]` para inverter uma string é muito elegante — não precisas de nenhum loop
- As f-strings suportam expressões dentro das `{}`, por exemplo `f'{2 ** 10}'` imprime `1024` diretamente
- `.find()` devolve `-1` se não encontrar, enquanto `.index()` lança uma exceção — importante saber a diferença

---

## ❓ Dúvidas que ficaram

<!-- Regista aqui o que ainda não ficou claro -->

---

## ⚠️ Armadilhas comuns

```python
# Strings são IMUTÁVEIS — isto dá erro:
nome = 'Jormaedes'
nome[0] = 'j'  # ❌ TypeError: 'str' object does not support item assignment

# Solução: cria uma nova string
nome = 'j' + nome[1:]  # ✅ 'jormaedes'
```