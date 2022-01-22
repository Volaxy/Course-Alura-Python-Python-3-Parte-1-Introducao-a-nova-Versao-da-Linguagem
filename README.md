# Python 3 parte 1: Introdução à nova versão da linguagem


Curso da Alura sobre a Parte 1 de Introdução ao Python

## Objetivo Final &#x1F3AF;

Criar um jogo de adivinhação, onde o computador irá escolher um número aleatório e o jogador terá que adivinhar esse número.

URL do curso -> [Python 3 parte 1: Introdução à nova versão da linguagem](https://cursos.alura.com.br/course/python-3-introducao-a-nova-versao-da-linguagem)

![Python 3 parte 1: Introdução à nova versão da linguagem](https://www.alura.com.br/assets/api/share/curso-python-3-introducao-a-nova-versao-da-linguagem.png)

## Links Úteis &#x1F517;
* [Python](https://www.python.org/) - Site oficial do pyhton.
* [Repl.it](https://replit.com/) - Site onde é possível programar com várias linguagens sem precisar instalar elas na máquina.
* [PyCharm](https://www.jetbrains.com/pycharm/) - Site da IDE PyCharm muito utilizada para o desenvolvimento de Python.

## Siglas &#x1F5FA;
* **REPL** - Sites onde se podem executar códigos de linguagem de de programação sem uma IDE específica ou instalar algum software.

## 01 - Introdução e Instalação do Python 3

### 01 - Função **`print`** e Variáveis
* `print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=false)` imprime algo na tela, a função pode receber 3 valores:
    * **`value`** é o valor que queremos imprimir, as reticências indicam que a função pode receber mais de um valor, basta separá-los por vírgula.
    * **`sep`** é o separador entre os valores, por padrão o separador é um espaço em branco.
    * **`end`** é o que acontecerá ao final da função, por padrão há uma quebra de linha, uma nova linha (**\n**).
* `help()` para obter a documentação na linha de comando e entrar no prompt de ajuda para obter ajuda com sintaxe dos comandos.
* A função `type()` retorna o tipo do valor da variável

### 02 - Tipagem do Python
O Python utiliza por convenção o padrão ***Snake_Case*** para nomes de variáveis (ou identificadores).

Um exemplo de variáveis em *Snake_Case* são:
```
idade_esposa = 20
perfil_vip = 'Flávio Almeida'
recibos_em_atraso = 30COPIAR CÓDIGO
```

Em outras linguagens também se usa o padrão `CamelCase`. O mesmo exemplo com `CamelCase` (que **não é** o padrão do Python):
```
idadeEsposa = 20
perfilVip = 'Flávio Almeida'
recibosEmAtraso = 30COP
```

## 02 - Lidando com a Entrada do Usuário

### 02 - Comparando Variáveis
* A função `input()` pode receber uma *string* passada por parâmetro e lê uma entrada do usuário até apertar o *ENTER*.
    * O retorno do usuário **sempre** será uma *string*.
* Para marcar o fim da instrução e início de um bloco (o código que será executado caso a condição seja verdadeira ou falsa), é utilizado dois pontos (`:`).
* O código que será executado caso a condição seja verdadeira ou falsa deve estar indentada dentro do bloco `if`.
* Para converter um valor de qualquer tipo para o tipo *int*, se usa a função `int()`, onde o valor é passado por parâmetro.
* O **Python** não consegue somar uma *string* com um *int*. `Ex.: 10 + "10"`.
* O **Python** possui um recurso chamado ***syntax sugar***, que simplifica algo que seria trabalhoso, como:
```
numero1 = 10
numero2 = "20"
produto = numero1 * numero2
print(produto)
```
Resultado: `20202020202020202020`


## 03 - Testando Valores

### 01 - A Condição elif
* O `elif` verifica se uma condição é verdadeira caso o `if` precedente seja falso.

## 04 - A Sequência do Jogo

### 02 - Formatação de Strings
* Existem 2 formas de se formatar uma string dentro de um `print()`, isso se chama **interpolação**:
    * `print("Tentativa {} de {}".format(rodada, total_de_tentativas))`, onde cada `{}` será substituido pela variável presente no `.format()`.
    * `print(f"Round {round_number} of {attempts}".)`, onde o nome da variável será substituido pelo valor da mesma.

## 05 - Iterando de Maneira Diferente

### 01 - O Laço com For
* O `for VARIABLE in range(START, STOP, STEP)` representa um loop onde:
    * **`VARIABLE`** é o nome da variável que será declarada para receber o valor do `range`.
    * **`range`** especifíca de qual valor deve iniciar e quando deve terminar.
    * **`STEP`** que pode ser opcional, onde o valor é incrementado pelo `STEP`.
    * O **`STOP`** é **exclusivo**, ou seja, o código é executado até **STOP - 1**.

### 03 - Formatação de Strings
* Para mudar a ordem de uma **interpolação**, basta digitar
```
print("Tentativa {1} de {0}".format(1, 3))

Tentativa 3 de 1
```
Onde os números indicam a ordem em que deve ser colocada as variáveis.

#### Formatação de Floats
* Exemplo básico:
```
>>> print("R$ {}".format(1.59))
R$ 1.59
```

* Para dizer que o número é um **float**:
```
>>> print("R$ {:f}".format(1.59))
R$ 1.590000
```

* Para dizer quantas casas decimais o número deve ter:
```
>>> print("R$ {:.2f}".format(1.59))
R$ 1.59
```
```
>>> print("R$ {:.2f}".format(1.5))
R$ 1.50
```

* Para deixar o **ponto** sempre na mesma coluna de caracteres:
```
>>> print("R$ {:7.2f}".format(1234.50))
R$ 1234.50
>>> print("R$ {:7.2f}".format(1.5))
R$    1.50
```
Onde o "7" significa o total de números.

* Para preencher os espaços em branco:
```
>>> print("R$ {:07.2f}".format(1.5))
R$ 0001.50
```

#### Formatação de Inteiros
* Exemplo básico:
```
>>> print("R$ {:07d}".format(4))
R$ 0000004
```

* Formatando uma data:
```
>>> print("Data {:02d}/{:02d}".format(9, 4))
Data 09/04
>>> print("Data {:02d}/{:02d}".format(19, 11))
Data 19/11
```

## 06 - Gerando Números Aleatórios

### 01 - Gerando e Arredondando um Número Aleatório
* A função `random.random()` gera um número aleatório entre 0.0 e 1.0.
* Para importar um módulo, basta digitar `>>> import random`.
* Para arredondar um número, usa-se `round()`.

### 02 - Definindo um Intervalo para a Geração de Número Aleatórios
* Para sortear um número inteiro entre um número e outro, usa-se `random.randrange(START, STOP)`