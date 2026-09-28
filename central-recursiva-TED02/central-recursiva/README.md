# Central Recursiva — TED 02

## Integrantes

- Gustavo Silva — RA: 26.1.15196
- Kaue Lima — RA: 26.1.19982

## Descrição

Projeto desenvolvido para a **TED 02 – Sistema de Algoritmos Recursivos, Módulos e Código Robusto**.

A aplicação implementa o problema **CentralRecursivaRobusta**, disponibilizado no beecrowd Academic. O sistema processa duas operações matemáticas:

- `M A B`: calcula o Máximo Divisor Comum (MDC) de `A` e `B`;
- `S N`: calcula a soma dos dígitos de `N`.

Os dois cálculos são realizados utilizando **recursividade**.

## Estrutura do projeto

```text
central-recursiva/
├── README.md
├── main.py
└── central/
    ├── __init__.py
    ├── algoritmos.py
    ├── validacoes.py
    └── excecoes.py
```

## Módulos desenvolvidos

### `main.py`

Responsável pela entrada de dados, identificação das operações, chamada das funções dos módulos e tratamento das exceções com `try`, `except` e `finally`.

### `central/algoritmos.py`

Contém os dois algoritmos recursivos da aplicação:

- `mdc(a, b)`
- `soma_digitos(n)`

### `central/validacoes.py`

Contém as funções responsáveis por validar os valores recebidos antes da realização dos cálculos.

### `central/excecoes.py`

Contém as exceções personalizadas utilizadas pelo sistema:

- `EntradaInvalidaError`
- `OperacaoInvalidaError`

As duas classes herdam de `Exception`.

## Algoritmos recursivos

### MDC — Algoritmo de Euclides

O MDC é calculado recursivamente. A cada chamada, o problema é reduzido para o MDC entre `b` e o resto de `a` dividido por `b`.

```python
def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)
```

Quando `b` chega a zero, `a` contém o MDC.

### Soma dos dígitos

A soma é calculada separando o último dígito com `% 10` e removendo esse dígito com divisão inteira `// 10`.

```python
def soma_digitos(n):
    if n == 0:
        return 0
    return (n % 10) + soma_digitos(n // 10)
```

Quando o número chega a zero, a recursão termina.

## Exceções personalizadas

A aplicação possui duas exceções:

### `EntradaInvalidaError`

Utilizada quando uma operação conhecida recebe valores inválidos. Exemplos:

- `M 0 25`
- `M -10 5`
- `S -50`

### `OperacaoInvalidaError`

Utilizada quando a operação informada é diferente de `M` ou `S`.

Exemplo:

```text
X 10 20
```

O programa utiliza `try`, `except` e `finally` para controlar essas situações.

## Como executar

É necessário possuir Python 3 instalado.

Na pasta principal do projeto, execute:

```bash
python main.py
```

Exemplo de entrada:

```text
7
S 12345
M 72 30
M 17 19
S 0
M 0 25
S -50
X 10 20
```

Saída esperada:

```text
SOMA = 15
MDC = 6
MDC = 1
SOMA = 0
ERRO: EntradaInvalida
ERRO: EntradaInvalida
ERRO: OperacaoInvalida
```

## Beecrowd

A lógica utilizada no projeto corresponde à solução submetida para o problema **CentralRecursivaRobusta** no beecrowd Academic.

A versão do repositório foi organizada em pacote e módulos para atender aos requisitos de modularização da TED 02.
