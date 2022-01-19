# Python 3 parte 1: Introdução à nova versão da linguagem


Curso da Alura sobre a Parte 1 de Introdução ao Python

## Objetivo Final &#x1F3AF;

Criar um jogo de adivinhação, onde o computador irá escolher um número aleatório e o jogador terá que adivinhar esse número.

URL do curso -> [Python 3 parte 1: Introdução à nova versão da linguagem](https://cursos.alura.com.br/course/python-3-introducao-a-nova-versao-da-linguagem)

![Python 3 parte 1: Introdução à nova versão da linguagem](https://www.alura.com.br/assets/api/share/curso-python-3-introducao-a-nova-versao-da-linguagem.png)

## Links Úteis &#x1F517;
* [Python](https://www.python.org/) - Site oficial do pyhton.
* [Repl.it](https://replit.com/) - Site onde é possível programar com várias linguagens sem precisar instalar elas na máquina.

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
